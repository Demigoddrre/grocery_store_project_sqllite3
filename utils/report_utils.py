import csv
import sqlite3
import matplotlib.pyplot as plt
from database.config import connect_to_db

def generate_report(report_type, time_period, output_path):
    """
    Generates a CSV report based on the report type and time period.

    :param report_type: The type of report to generate (e.g., 'earnings', 'product_performance').
    :param time_period: The time period for the report (e.g., 'monthly', 'quarterly', 'annually').
    :param output_path: The path where the report CSV file should be saved.
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
        elif report_type == "product_performance":
            query = """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
            """
        else:
            print("Invalid report type.")
            return

        # Execute query and fetch data
        cursor.execute(query)
        rows = cursor.fetchall()

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
    Generates a graph based on the graph type and time period.

    :param graph_type: The type of graph to generate (e.g., 'spending', 'product_performance').
    :param time_period: The time period for the graph (e.g., 'monthly', 'quarterly', 'annually').
    :param output_path: The path where the graph image should be saved.
    """
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        # Define SQL queries for different graph types
        if graph_type == "spending":
            query = """
                SELECT 
                    p.Category AS Category,
                    SUM(od.Price * od.Quantity) AS TotalSpending
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.Category
            """
            x_label = "Category"
            y_label = "Total Spending"
        elif graph_type == "product_performance":
            query = """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
            """
            x_label = "Product Name"
            y_label = "Total Sold"
        else:
            print("Invalid graph type.")
            return

        # Execute query and fetch data
        cursor.execute(query)
        rows = cursor.fetchall()

        # Prepare data for plotting
        x_data = [row[0] for row in rows]
        y_data = [row[1] for row in rows]

        # Plot graph using matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(x_data, y_data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f"{graph_type.capitalize()} Graph")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

        print(f"Graph saved at {output_path}.")
    except Exception as e:
        print(f"Error generating graph: {e}")
    finally:
        cursor.close()
        conn.close()
