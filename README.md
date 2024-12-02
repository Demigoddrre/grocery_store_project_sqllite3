
# Grocery Store Management System

A Python-based console application designed for grocery store operations, allowing users to generate reports, view visualizations, and manage data efficiently.

---

## Features
- **Generate Reports**: Earnings, spending, product performance, and least-selling reports saved as CSV files.
- **Power BI Integration**: Upload and view reports in Power BI for interactive analytics.
- **Email Integration**: (Planned) Send reports via email using SendGrid.
- **Database Operations**: Execute inventory updates and calculate loyalty points.

---

## Installation and Setup

### Prerequisites
Ensure the following are installed:
- **Python 3.x** and **pip**
- **SQLite 3** (default with Python installation)
- Internet connection (for Power BI API and future SendGrid integration)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd grocery_store_project_sqllite3
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

#### 5. Configure Power BI (Optional for Power BI Integration)
- Set up Power BI and Azure AD for REST API access.
- Obtain **Client ID**, **Client Secret**, **Tenant ID**, and **Workspace ID**.
- Add these to your `power_bi_config` dictionary in `menu_functions.py`.

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
├── templates/                      # Web templates for embedded Power BI
│   ├── report_viewer.html          # Power BI embedded report viewer
├── utils/
│   ├── db_utils.py                 # Utility functions for database operations
│   ├── report_utils.py             # Reporting and Power BI utilities
│   ├── power_bi_utils.py           # Power BI REST API helper functions
│   ├── send_email.py               # Email integration (Planned)
├── web_app.py                      # Flask app for displaying Power BI reports
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
1. **Generate Reports**: Create CSV files for various report types (e.g., earnings, spending).
2. **Upload and View Power BI Reports**: Automatically upload reports to Power BI and view in a browser.
3. **Send Reports via Email**: (Planned) Email reports using SendGrid integration.
4. **Execute Operations**: Manage inventory, loyalty points, and other operations.
5. **Exit**: Close the application.

### Example Workflow
1. Run the application: `python3 main.py`.
2. Select **1. Generate Report** and specify the type (`earnings`, `spending`) and time period.
3. Select **2. Upload and View Power BI Reports** to integrate reports into Power BI.
4. View reports interactively in a browser window using Flask.

---

## Troubleshooting

### Known Issues
1. **Power BI Configuration**:
   - Ensure correct API credentials are used for Power BI.
   - Use a Windows environment if running Power BI Desktop locally.

2. **File Generation Errors**:
   - Validate that generated CSV files exist before uploading to Power BI.

3. **Unclear Input Options**:
   - Menu currently doesn't list valid options for report types. This needs improvement.

4. **Incomplete Features**:
   - Email functionality is not yet implemented.

---

### General Debugging Tips

#### Database Issues
- Ensure `create_tables.py` has been run to create necessary tables.
- Check the database path in `database/config.py`:
  ```python
  def connect_to_db():
      return sqlite3.connect("database/grocery_store.db")
  ```

#### Power BI Errors
- Ensure you have set up Power BI credentials correctly.
- Confirm the workspace and dataset IDs match your Power BI settings.

---

## Recent Updates
1. **Power BI Integration**:
   - Added functionality to upload and embed CSV reports into Power BI dashboards.
   - Users can now view reports interactively in a browser.

2. **Dynamic Report Naming**:
   - Reports are now named dynamically based on the report type and time period (e.g., `earnings_monthly.csv`, `spending_quarterly.csv`).

3. **Error Handling**:
   - Improved error handling for missing files, empty datasets, and unsupported input.

---

## Future Enhancements
1. **Email Integration**:
   - Implement functionality to email reports or graphs to users.

2. **Input Validation**:
   - Validate user input in the menu to prevent unsupported or invalid options.

3. **Automated Testing**:
   - Add unit tests for report generation and Power BI integration.

4. **Graph Alternatives**:
   - Replace `matplotlib` entirely with Power BI for data visualization.

---

## To-Do List

### Immediate Fixes
1. Validate the Power BI integration workflow:
   - Ensure CSV uploads are seamless.
   - Confirm embedded report URLs display correctly.

2. Improve user feedback in the menu:
   - Clearly list valid options for report and graph types.

3. Add basic input validation for menu options.

---

## Author
Developed by D'Andre D.

Happy managing! 🚀

---
```