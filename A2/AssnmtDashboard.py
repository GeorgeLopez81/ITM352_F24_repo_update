import pandas as pd
import pyarrow
import time
import sys

# Load and preprocess the data
def load_csv(file_path):
    try:
        print(f"Loading data from: {file_path}")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")
        print(f"Columns available: {sales_data.columns.to_list()}")

        required_columns = ['quantity', 'order_date', 'unit_price', 'sales_region', 'order_type', 'customer_type', 'product', 'employee_id']
        missing_columns = [col for col in required_columns if col not in sales_data.columns]
        
        if missing_columns:
            print(f"Warning: Missing columns: {missing_columns}. Some analytics may not work.")
        
        sales_data.fillna(0, inplace=True)
        sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], errors='coerce')
        sales_data['total_sales'] = sales_data['quantity'] * sales_data['unit_price']  # Calculate total sales per row
        return sales_data

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Exiting.")
        sys.exit(1)

def ask_export(data):
    export_choice = input("Would you like to export this result to an Excel file? (yes/no): ").strip().lower()
    if export_choice == 'yes':
        filename = input("Enter the filename (with .xlsx extension): ").strip()
        data.to_excel(filename, index=True)
        print(f"Data exported successfully to {filename}")

# New Sales Trend Analysis Function
def sales_trends_over_time(data):
    print("\n--- Sales Trends Over Time ---")
    print("Choose a time aggregation level:")
    print("1. Monthly")
    print("2. Quarterly")
    print("3. Yearly")
    time_choice = input("Your choice (1/2/3): ").strip()

    # Aggregate data based on the selected time period
    if time_choice == '1':
        data['period'] = data['order_date'].dt.to_period('M')
        aggregation_level = 'Monthly'
    elif time_choice == '2':
        data['period'] = data['order_date'].dt.to_period('Q')
        aggregation_level = 'Quarterly'
    elif time_choice == '3':
        data['period'] = data['order_date'].dt.to_period('Y')
        aggregation_level = 'Yearly'
    else:
        print("Invalid choice. Returning to main menu.")
        return

    result = pd.pivot_table(data, values='total_sales', index='period', aggfunc='sum')
    print(f"\nTotal Sales ({aggregation_level})")
    print(result)
    ask_export(result)

# Menu functions (existing ones)
def show_n_rows(data):
    try:
        num_rows = len(data)
        print(f"\nTotal rows available: {num_rows}")
        choice = input("Enter number of rows to display (or 'all' to see all rows): ").strip().lower()
        if choice == 'all':
            display_data = data
        elif choice.isdigit() and 1 <= int(choice) <= num_rows:
            display_data = data.head(int(choice))
        else:
            print("Invalid input. Displaying first 5 rows by default.")
            display_data = data.head(5)
        print(display_data)
        ask_export(display_data)
    except ValueError:
        print("Invalid input. Please try again.")

def total_sales_by_region_order_type(data):
    result = pd.pivot_table(data, values='unit_price', index='sales_region', columns='order_type', aggfunc='sum')
    print(result)
    ask_export(result)

def avg_sales_by_region_state_type(data):
    result = pd.pivot_table(data, values='unit_price', index='sales_region', columns=['order_type'], aggfunc='mean')
    print(result)
    ask_export(result)

def sales_by_customer_type_order_type_state(data):
    result = pd.pivot_table(data, values='unit_price', index=['customer_type', 'order_type'], columns='sales_region', aggfunc='sum')
    print(result)
    ask_export(result)

def total_sales_qty_price_by_region_product(data):
    result = pd.pivot_table(data, values=['quantity', 'unit_price'], index='sales_region', columns='product', aggfunc='sum')
    print(result)
    ask_export(result)

def total_sales_qty_price_by_customer_type(data):
    result = pd.pivot_table(data, values=['quantity', 'unit_price'], index='customer_type', columns='order_type', aggfunc='sum')
    print(result)
    ask_export(result)

def max_min_sales_price_by_category(data):
    result = pd.pivot_table(data, values='unit_price', index='product', aggfunc={'unit_price': ['max', 'min']})
    print(result)
    ask_export(result)

def unique_employees_by_region(data):
    result = pd.pivot_table(data, index="sales_region", values="employee_id", aggfunc=pd.Series.nunique)
    result.columns = ['Number of Employees']
    print(result)
    ask_export(result)

def create_custom_pivot_table(data):
    rows = input("Enter row fields (comma separated, e.g., 'sales_region,employee_id'): ").strip().split(',')
    columns = input("Enter column fields (optional, comma separated, e.g., 'order_type,customer_type'): ").strip().split(',')
    values = input("Enter values field (e.g., 'quantity' or 'unit_price'): ").strip()
    agg_func = input("Choose aggregation function (sum, mean, count): ").strip().lower()
    if agg_func not in ['sum', 'mean', 'count']:
        print("Invalid aggregation function. Defaulting to 'sum'")
        agg_func = 'sum'
    result = pd.pivot_table(data, values=values, index=rows, columns=columns if columns != [''] else None, aggfunc=agg_func)
    print(result)
    ask_export(result)

# Menu display
def display_menu(data):
    menu = {
        "1": ("Show the first n rows of sales data", show_n_rows),
        "2": ("Total sales by region and order_type", total_sales_by_region_order_type),
        "3": ("Average sales by region with average sales by state and sale type", avg_sales_by_region_state_type),
        "4": ("Sales by customer type and order type by state", sales_by_customer_type_order_type_state),
        "5": ("Total sales quantity and price by region and product", total_sales_qty_price_by_region_product),
        "6": ("Total sales quantity and price by customer type", total_sales_qty_price_by_customer_type),
        "7": ("Max and min sales price of sales by category", max_min_sales_price_by_category),
        "8": ("Number of unique employees by region", unique_employees_by_region),
        "9": ("Create a custom pivot table", create_custom_pivot_table),
        "10": ("Sales trends over time", sales_trends_over_time),  # New analytic function
        "11": ("Exit", exit_program)
    }
    while True:
        print("\n--- Sales Data Dashboard ---")
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")
        choice = input("Choose an option: ").strip()
        if choice in menu:
            menu[choice][1](data)
        else:
            print("Invalid selection. Please try again.")

# Exit program
def exit_program(data):
    print("Exiting program.")
    sys.exit(0)

# Load data and start the main loop
if __name__ == "__main__":
    file_path = "/Users/georgelopez/Desktop/ITM352_F24_repo/ITM352_F24_repo_update/ITM352_F24_repo_update/ITM352_F24_repo_update/ITM352_F24_repo_update/ITM352_F24_repo_update/ITM352_F24_repo_update-1/A2/sales_data (1).csv"  # Use your local file here
    sales_data = load_csv(file_path)
    if sales_data is not None:
        display_menu(sales_data)
