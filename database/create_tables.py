from config import connect_to_db

def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Create Products Table
    create_products_table = """
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT NOT NULL,
        Category TEXT,
        Price REAL NOT NULL,
        StockQuantity INTEGER NOT NULL,
        SupplierID INTEGER
    );
    """

    # Create Customers Table
    create_customers_table = """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email TEXT UNIQUE,
        LoyaltyPoints INTEGER DEFAULT 0
    );
    """

    # Create Orders Table
    create_orders_table = """
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        TotalAmount REAL NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    );
    """

    # Create OrderDetails Table
    create_orderdetails_table = """
    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER NOT NULL,
        Price REAL NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );
    """

    # Create Suppliers Table
    create_suppliers_table = """
    CREATE TABLE IF NOT EXISTS Suppliers (
        SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
        SupplierName TEXT NOT NULL,
        ContactInfo TEXT
    );
    """

    # Execute SQL commands
    cursor.execute(create_products_table)
    cursor.execute(create_customers_table)
    cursor.execute(create_orders_table)
    cursor.execute(create_orderdetails_table)
    cursor.execute(create_suppliers_table)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
