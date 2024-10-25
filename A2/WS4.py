#Allow users to interactively explore and analyze sales data from a CSV file by 
#providing a simple command-lin interface.
import pandas as pd
import pyarrow 
import ssl
import time
import sys


ssl._create_default_https_context = ssl._create_unverified_context # this is used to override if i get a certificat error

#set the display to show all columns
#pd.set_option("display.max_columns", None)
pd.set_option("display.max_columns", None)

#import the data file. this needs to be downloaded to be used by pandas

def load_csv(file_path):

    #attempt to read the CSV file
    try:
        print("Reading CSV file...")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time
        print(f"File laoded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")
        print(f"Columns: {sales_data.columns.to_list()}")

    #List the required columns
    required_columns = ['quantity', 'order_date', 'unit_price']

    #Check for missing columns
    missing_columns = [col for col in required_columns not in sales_data.columns]

    if missing_columns:
        print("\nWarning: The following required columns are missing: {missing_columns}")

    else:
        print(f"\nAll required columns are present ")

    #Ask Pandas to parse the order_date field into a standard representation
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format="mixed")

    #Save the first 10 rows of the data in sales_data_test.csv
    sales_data.head(10).to_csv('sales_data_test.csv')

    return sales_data

except FileNotFoundError:
    print(f"Error: the file {file_path} was not found.")
except pd.errors.EmtyDataError as e: 
        print(f"Error: the file {file_path} was not empty.")
except pd.errors.ParseError as e:
    print(f"Error: there was a problem parsing {file_path}.")

except Exception as e:
    print(f"An unexpected error has occurred: {e}")

#Function to display a suser choosable number of rows 
def display_rows(data):
     while True:
          numRows= len(data)-1
          print("\nEnter number of rows to display:")
          print(f"-Enter a number between 1 and {numRows}")
          print("-To see all rows enter 'all")
          print("-To skip, press Enter")
          user_choice = input("Your choice: ").strip(). lower()

          if user_choice=='':
            print("Skipping preview")
            break
          elif user_choice == 'all':
            print(data)
            break
          elif user_choice.isdigit() and 1<=int(user_choice) <= numRows:
            print(data.head(int(user_choice)))
            break
          else:
              print("Invalid input. Please re-enter.")
 #Cleanly exit the program         
 def exit_program(data):
    sys.exit(0)   

def display_menu(data): 
    menu_option= (
        ("Shows the first n rows of data", display_rows),
        ("Show the number of employees by region", employees_by_region),
        ("Exit the program", exit_program)
    )
    print("\nPlease choos from among these options:")
    for index, (description, _) in enumerate(menu_option): 
        print(f"{index+1}: {description}")

    num_choices = len(menu_options)
    choice = int(input(f"Select an option between 1 and {num_choices}: "))

    if 1<= choice <= num_choices:
        action = menu_option[choice-1][1]
        action(data)
    else:
        print("Invalid input. Please re-enter.")

#print the number of unique employees per region
def employee_by_region(data):
   pivot_table= pd.pivot_table(data, index="sales_region", values="employee_id", 
                               aggfunc=pd.Series.nunique)
   print("\nNumber of Employees by Region")
   pivot_table.columns= ['Number of Employees'] #Rename the column for readability
   print(pivot_table)
   return pivot_table


#call load _csv to load the file
url = "https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
#url='sales_data.csv'
sales_data =load_csv(url)

#Main loop for user interation
def main():
     while True:
          display_menue(sales_data)

    
#If this is the main program, call main()
if __name__ == "__main":
     main()