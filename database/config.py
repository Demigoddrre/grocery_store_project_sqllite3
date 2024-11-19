import sqlite3
import os

# Define the database directory and path
DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "grocery_store.db")

# Ensure the directory exists
os.makedirs(DB_DIR, exist_ok=True)

def connect_to_db():
    """Creates a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)
