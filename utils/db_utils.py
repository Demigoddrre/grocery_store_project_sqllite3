from database.config import connect_to_db

def update_inventory(product_id, quantity):
    """Simulates updating inventory after a purchase."""
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE Products SET StockQuantity = StockQuantity - ? WHERE ProductID = ?",
            (quantity, product_id)
        )
        conn.commit()
        print(f"Inventory updated for Product ID {product_id}.")
    except Exception as e:
        print(f"Error updating inventory: {e}")
    finally:
        cursor.close()
        conn.close()

def calculate_loyalty_points(customer_id, total_amount):
    """Simulates calculating loyalty points."""
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        points = total_amount // 10  # 1 point for every $10 spent
        cursor.execute(
            "UPDATE Customers SET LoyaltyPoints = LoyaltyPoints + ? WHERE CustomerID = ?",
            (points, customer_id)
        )
        conn.commit()
        print(f"Loyalty points updated for Customer ID {customer_id}.")
    except Exception as e:
        print(f"Error calculating loyalty points: {e}")
    finally:
        cursor.close()
        conn.close()
