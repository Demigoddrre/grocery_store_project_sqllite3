
---

# Grocery Store Management System

A Python-based console application designed for grocery store operations, allowing users to generate reports, view visualizations, and manage data efficiently.

---

## Features
- **Generate Reports**: Earnings and spending reports saved as CSV files.
- **Data Visualizations**: Spending and earnings graphs saved as PNG images.
- **Email Integration**: (Planned) Send reports via email using SendGrid.
- **Database Operations**: Execute inventory updates and calculate loyalty points.

---

## Installation and Setup

### Prerequisites
Ensure the following are installed:
- **Python 3.x** and **pip**
- **SQLite 3** (default with Python installation)
- Internet connection (for future SendGrid API integration)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd grocery_store_project
```

#### 2. Install Dependencies
Install the Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 3. Set Up the Database
Create the necessary tables:
```bash
python3 database/create_tables.py
```
This script will initialize the database in `database/grocery_store.db`.

#### 4. Populate Test Data (Optional)
Add sample data to the database for testing:
```bash
python3 database/populate_test_data.py
```

---

## Project Structure

```
grocery_store_project/
├── database/
│   ├── grocery_store.db            # SQLite database file
│   ├── config.py                   # Database connection logic
│   ├── create_tables.py            # Schema creation script
│   ├── populate_test_data.py       # Test data population script
├── reports/
│   ├── csv/                        # Directory for CSV reports
│   │   ├── earnings_monthly.csv    # Example: Monthly earnings report
│   │   ├── spending_monthly.csv    # Example: Monthly spending report
│   ├── graphs/                     # Directory for graph images
│       ├── spending_monthly.png    # Example: Monthly spending graph
├── utils/
│   ├── db_utils.py                 # Utility functions for database operations
│   ├── report_utils.py             # Reporting and visualization utilities
├── main.py                         # Entry point for the application
├── menu_functions.py               # User interaction and menu logic
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (not tracked in Git)
```

---

## Usage

### Run the Application
Start the console-based management system:
```bash
python3 main.py
```

### Available Menu Options
1. **Generate Reports**: Create CSV files for earnings or spending reports.
2. **View Graphs**: Generate visualizations for earnings or spending data.
3. **Send Reports via Email**: (Planned) Email reports using SendGrid integration.
4. **Execute Operations**: Manage inventory, loyalty points, and other operations.
5. **Exit**: Close the application.

### Example Workflow
1. Run the application: `python3 main.py`.
2. Select **1. Generate Report** and specify the type (`earnings`, `spending`) and time period.
3. Select **2. View Graphs** to generate a visualization.
4. Save generated graphs as `.png` files and optionally display them interactively.

---

## Troubleshooting

### Known Issues
1. **Graph Generation Errors**:
   - Inconsistent behavior where graphs are not displayed interactively or saved correctly as `.png` files.
   - Occasionally throws errors such as "CSV file not found" despite the file existing.

2. **Unclear Input Options**:
   - Users are not clearly informed about valid report or graph types (e.g., `earnings`, `spending`).

3. **Incomplete Features**:
   - Email functionality is not yet implemented.
   - No validation for invalid user input, which could cause unexpected errors.

---

### General Debugging Tips

#### Database Issues
- Ensure `create_tables.py` has been run to create necessary tables.
- Check the database path in `database/config.py`:
  ```python
  def connect_to_db():
      return sqlite3.connect("database/grocery_store.db")
  ```

#### Graph or Report Errors
- Confirm data exists in the database tables using SQLite CLI:
  ```bash
  sqlite3 database/grocery_store.db
  sqlite> SELECT * FROM Orders;
  ```

---

## Recent Updates
1. **Dynamic Report Naming**:
   - Reports are now named dynamically based on the report type and time period (e.g., `earnings_monthly.csv`, `spending_quarterly.csv`).

2. **Error Handling**:
   - Improved error handling for missing files, empty datasets, and unsupported input.

3. **Graph Functionality**:
   - Added an option to save graphs as `.png` files and display them interactively.

---

## Future Enhancements
1. **Email Integration**:
   - Implement functionality to email reports or graphs to users.

2. **Additional Report Types**:
   - Add new reports for best-selling products, low-stock alerts, and customer trends.

3. **Input Validation**:
   - Validate user input in the menu to prevent unsupported or invalid options.

4. **Automated Testing**:
   - Add unit tests for report generation and graphing functionality.

5. **Database Migration**:
   - Explore transitioning to a scalable database like PostgreSQL for production use.

---

## To-Do List

### Immediate Fixes
1. Debug the graph generation process to ensure:
   - Files save correctly.
   - Graphs display interactively as intended.

2. Improve user feedback in the menu:
   - Clearly list valid options for report and graph types.

3. Add basic validation for user input.

### Next Steps
1. Implement the email feature using SendGrid.
2. Enhance reporting functionality with additional report types.
3. Introduce automated testing for critical functions.

---

## Author
Developed by D'Andre D.

Happy managing! 🚀

---
