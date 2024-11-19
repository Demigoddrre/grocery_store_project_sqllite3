from utils.report_utils import generate_report, view_graphs
from utils.db_utils import update_inventory, calculate_loyalty_points
from utils.send_email import send_email_with_attachment
import os

def generate_report_menu():
    print("\n=== Generate Report ===")
    report_type = input("Enter report type (e.g., earnings, product performance): ")
    time_period = input("Enter time period (e.g., monthly, quarterly, annually): ")
    output_path = f"reports/csv/{report_type}_{time_period}.csv"
    generate_report(report_type, time_period, output_path)
    print(f"Report saved to {output_path}.")

def view_graphs_menu():
    print("\n=== View Graphs ===")
    graph_type = input("Enter graph type (e.g., spending, product performance): ")
    time_period = input("Enter time period (e.g., monthly, quarterly, annually): ")
    output_path = f"reports/graphs/{graph_type}_{time_period}.png"
    view_graphs(graph_type, time_period, output_path)
    print(f"Graph saved to {output_path}.")

def send_reports_menu():
    print("\n=== Send Reports via Email ===")
    send_email_with_attachment()  # This now dynamically collects details from the user.

def execute_operations_menu():
    print("\n=== Execute Predefined Operations ===")
    print("1. Update Inventory After Purchase")
    print("2. Calculate Loyalty Points")
    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity Purchased: "))
        update_inventory(product_id, quantity)
    elif choice == "2":
        customer_id = int(input("Enter Customer ID: "))
        total_amount = float(input("Enter Total Amount Spent: "))
        calculate_loyalty_points(customer_id, total_amount)
    else:
        print("Invalid choice. Returning to main menu.")

def main_menu():
    while True:
        print("\n=== Grocery Store Management Console ===")
        print("1. Generate Report")
        print("2. View Graphs")
        print("3. Send Reports via Email")
        print("4. Execute Predefined Operations (e.g., Update Inventory, Calculate Loyalty Points)")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            generate_report_menu()
        elif choice == "2":
            view_graphs_menu()
        elif choice == "3":
            send_reports_menu()  # Calls the updated email sending function.
        elif choice == "4":
            execute_operations_menu()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
