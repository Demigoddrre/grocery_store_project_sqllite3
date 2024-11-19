import random
import sqlite3
from datetime import datetime, timedelta
from config import connect_to_db

def populate_test_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        # Insert Suppliers
        suppliers = [
            ('Fresh Farms', '123-456-7890'),
            ('Dairy World', '987-654-3210'),
            ('Grain Supplies', '555-123-4567'),
            ('Seafood Distributors', '444-789-0123')
        ]
        cursor.executemany("INSERT INTO Suppliers (SupplierName, ContactInfo) VALUES (?, ?)", suppliers)

        # Insert Products
        products = [
            ('Apple', 'Fruits', 0.5, 100, 1),
            ('Milk', 'Dairy', 1.2, 50, 2),
            ('Bread', 'Grains', 2.0, 200, 3),
            ('Salmon', 'Seafood', 10.0, 30, 4),
            ('Eggs', 'Dairy', 3.0, 150, 2),
            ('Banana', 'Fruits', 0.3, 120, 1),
            ('Cheese', 'Dairy', 4.5, 40, 2),
            ('Chicken', 'Meat', 7.5, 60, 4),
            ('Rice', 'Grains', 1.8, 300, 3)
        ]
        cursor.executemany("INSERT INTO Products (ProductName, Category, Price, StockQuantity, SupplierID) VALUES (?, ?, ?, ?, ?)", products)

        # Insert Customers
        customers = [
            ('John', 'Doe', 'john.doe@example.com', 50),
            ('Jane', 'Smith', 'jane.smith@example.com', 100),
            ('Alice', 'Johnson', 'alice.johnson@example.com', 200),
            ('Bob', 'Brown', 'bob.brown@example.com', 80)
        ]
        cursor.executemany("INSERT INTO Customers (FirstName, LastName, Email, LoyaltyPoints) VALUES (?, ?, ?, ?)", customers)

        # Insert Orders
        start_date = datetime(2024, 1, 1)
        orders = []
        for i in range(1, 51):  # Generate 50 orders
            customer_id = random.randint(1, len(customers))
            order_date = start_date + timedelta(days=random.randint(0, 300))
            total_amount = round(random.uniform(20, 200), 2)
            orders.append((customer_id, total_amount, order_date.strftime('%Y-%m-%d')))

        cursor.executemany("INSERT INTO Orders (CustomerID, TotalAmount, OrderDate) VALUES (?, ?, ?)", orders)

        # Insert Order Details
        order_details = []
        for order_id in range(1, 51):  # Generate order details for the 50 orders
            num_items = random.randint(1, 5)
            for _ in range(num_items):
                product_id = random.randint(1, len(products))
                quantity = random.randint(1, 10)
                cursor.execute("SELECT Price FROM Products WHERE ProductID = ?", (product_id,))
                price = cursor.fetchone()[0]
                order_details.append((order_id, product_id, quantity, price))

        cursor.executemany("INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES (?, ?, ?, ?)", order_details)

        conn.commit()
        print("Test data populated successfully!")
    except Exception as e:
        print(f"Error populating test data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    populate_test_data()
