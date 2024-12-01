import os
import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from database.config import connect_to_db

def generate_report(report_type, time_period, output_path=None):
    """
    Generates a CSV report based on the report type and time period.

    :param report_type: The type of report to generate (e.g., 'earnings', 'spending', 'product_performance', 'least_selling').
    :param time_period: The time period for the report (e.g., 'monthly', 'quarterly', 'annually').
    :param output_path: Optional, the path where the report CSV file should be saved.
    """
    conn = connect_to_db()

    cursor = conn.cursor()

    try:
        # Define SQL queries for different report types
        if report_type == "earnings":
            query = """
                SELECT 
                    DATE(OrderDate) AS OrderDate,
                    SUM(TotalAmount) AS TotalEarnings
                FROM Orders
                GROUP BY DATE(OrderDate)
            """
        elif report_type == "spending":
            query = """
                SELECT 
                    p.Category AS Category,
                    SUM(od.Price * od.Quantity) AS TotalSpending
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.Category
            """
        elif report_type == "product_performance":
            query = """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold,
                    SUM(od.Price * od.Quantity) AS TotalRevenue
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
                ORDER BY TotalSold DESC
            """
        elif report_type == "least_selling":
            query = """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
                HAVING TotalSold > 0
                ORDER BY TotalSold ASC
            """
        else:
            print("Invalid report type.")
            return

        # Execute query and fetch data
        cursor.execute(query)
        rows = cursor.fetchall()

        # Dynamically generate the correct CSV file name if not provided
        if not output_path:
            output_path = f"reports/csv/{report_type}_{time_period}.csv"

        # Write data to CSV file
        with open(output_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([desc[0] for desc in cursor.description])  # Write headers
            writer.writerows(rows)

        print(f"Report generated at {output_path}.")
    except Exception as e:
        print(f"Error generating report: {e}")
    finally:
        cursor.close()
        conn.close()


def view_graphs(graph_type, time_period, output_path):
    """
    Generates a graph based on the report CSV files.

    :param graph_type: The type of graph to generate (e.g., 'earnings', 'spending').
    :param time_period: The time period for the graph (e.g., 'monthly', 'quarterly').
    :param output_path: The path where the graph image should be saved.
    """
    # Determine the correct CSV file path
    csv_file_path = f"reports/csv/{graph_type}_{time_period}.csv"

    try:
        # Check if the CSV file exists
        if not os.path.exists(csv_file_path):
            print(f"Error: The CSV file {csv_file_path} does not exist. Please generate the report first.")
            return

        # Load the CSV file
        data = pd.read_csv(csv_file_path)
        print(f"Loaded data from {csv_file_path}:\n{data.head()}")

        # Define the graph parameters based on the graph type
        if graph_type == "earnings":
            x_data = data['OrderDate']
            y_data = data['TotalEarnings']
            x_label = "Date"
            y_label = "Total Earnings"
            title = "Earnings Over Time"
        elif graph_type == "spending":
            x_data = data['Category']
            y_data = data['TotalSpending']
            x_label = "Category"
            y_label = "Total Spending"
            title = "Spending by Category"
        else:
            print("Invalid graph type specified.")
            return

        # Check if data exists
        if x_data.empty or y_data.empty:
            print("No data available to generate the graph.")
            return

        # Create the graph
        plt.figure(figsize=(10, 6))
        plt.bar(x_data, y_data, color='skyblue')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Save the graph to a file
        plt.savefig(output_path)
        print(f"Graph saved at {output_path}.")

        # Display the graph interactively
        plt.show()

    except FileNotFoundError:
        print(f"Error: The CSV file {csv_file_path} does not exist. Please generate the report first.")
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file {csv_file_path} is empty. Please check the report generation.")
    except Exception as e:
        print(f"Error generating graph: {e}")
