from utils.report_utils import generate_report, upload_and_refresh_report
from utils.db_utils import update_inventory, calculate_loyalty_points
from utils.send_email import send_email_with_attachment

def generate_report_menu():
    """
    Handles user input for generating a report.
    """
    print("\n=== Generate Report ===")
    report_type = input("Enter report type (e.g., earnings, spending, product_performance, least_selling): ")
    time_period = input("Enter time period (e.g., monthly, quarterly, annually): ")
    output_path = f"reports/csv/{report_type}_{time_period}.csv"
    generate_report(report_type, time_period, output_path)
    print(f"Report saved to {output_path}.")

def upload_and_view_report_menu():
    """
    Handles user input for refreshing Power BI reports.
    """
    print("\n=== Refresh Power BI Report ===")
    report_type = input("Enter report type (e.g., earnings, spending, product_performance, least_selling): ")
    time_period = input("Enter time period (e.g., monthly, quarterly, annually): ")
    
    power_bi_config = {
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "tenant_id": "your_tenant_id",
        "group_id": "your_group_id",
        "dataset_id": "your_dataset_id",
        "embed_url": "your_report_embed_url"
    }

    upload_and_refresh_report(report_type, time_period, power_bi_config)

def main_menu():
    """
    Main menu loop for the Grocery Store Management Console.
    """
    while True:
        print("\n=== Grocery Store Management Console ===")
        print("1. Generate Report")
        print("2. Upload and Refresh Power BI Report")
        print("3. Send Reports via Email")
        print("4. Execute Predefined Operations (e.g., Update Inventory, Calculate Loyalty Points)")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            generate_report_menu()
        elif choice == "2":
            upload_and_view_report_menu()
        elif choice == "3":
            send_reports_menu()
        elif choice == "4":
            execute_operations_menu()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
