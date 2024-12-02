import os
import csv
import sqlite3
from database.config import connect_to_db
from utils.power_bi_utils import get_power_bi_token, update_dataset

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
        queries = {
            "earnings": """
                SELECT 
                    DATE(OrderDate) AS OrderDate,
                    SUM(TotalAmount) AS TotalEarnings
                FROM Orders
                GROUP BY DATE(OrderDate)
            """,
            "spending": """
                SELECT 
                    p.Category AS Category,
                    SUM(od.Price * od.Quantity) AS TotalSpending
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.Category
            """,
            "product_performance": """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold,
                    SUM(od.Price * od.Quantity) AS TotalRevenue
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
                ORDER BY TotalSold DESC
            """,
            "least_selling": """
                SELECT 
                    p.ProductName AS ProductName,
                    SUM(od.Quantity) AS TotalSold
                FROM OrderDetails od
                JOIN Products p ON od.ProductID = p.ProductID
                GROUP BY p.ProductID
                HAVING TotalSold > 0
                ORDER BY TotalSold ASC
            """
        }

        if report_type not in queries:
            print("Invalid report type.")
            return

        # Execute the query
        query = queries[report_type]
        cursor.execute(query)
        rows = cursor.fetchall()

        # Generate CSV file
        if not output_path:
            output_path = f"reports/csv/{report_type}_{time_period}.csv"
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

def upload_and_refresh_report(report_type, time_period, power_bi_config):
    """
    Refreshes the Power BI dataset and ensures the report reflects updated data.

    :param report_type: The type of report (e.g., 'earnings', 'spending').
    :param time_period: The time period for the report (e.g., 'monthly', 'quarterly').
    :param power_bi_config: Dictionary containing Power BI credentials and configuration.
    """
    csv_file_path = f"reports/csv/{report_type}_{time_period}.csv"
    report_name = f"{report_type.capitalize()} {time_period.capitalize()}"

    if not os.path.exists(csv_file_path):
        print(f"Error: The CSV file {csv_file_path} does not exist. Please generate the report first.")
        return

    try:
        access_token = get_power_bi_token(
            power_bi_config["client_id"], 
            power_bi_config["client_secret"], 
            power_bi_config["tenant_id"]
        )
        update_dataset(
            access_token, 
            power_bi_config["group_id"], 
            power_bi_config["dataset_id"], 
            csv_file_path
        )
        print("Dataset updated successfully.")
        print(f"View the updated report here: {power_bi_config['embed_url']}")
    except Exception as e:
        print(f"Error refreshing report: {e}")
