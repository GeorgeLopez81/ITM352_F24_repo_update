#Read a file from a URL and write a local file "sales_data_test.csv"
#containing just the first 10 rows of data
import pandas as pd
#import pyarrow #not needed here
import ssl



ssl._create_default_https_context = ssl._create_unverified_context # this is used to override if i get a certificat error

#Import the data file. This needs to be downloaded to be used by Pandas. It is in CSV format.

# It is in CSV format.
file_id = "1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

#attempt to read the CSV file
try:
    print("Reading CSV file...")
    sales_data = pd.read_csv(url,on_bad_lines="skip")

#Ask Pandas to parse the order_date field into a standard representation
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format="mixed")

#Save the first 10 rows of the data in sales_data_test.csv
sales_data.head(10).to_csv('sales_data_test.csv')

except Exception as e:
    print(f"An error has ocurred :{e}")