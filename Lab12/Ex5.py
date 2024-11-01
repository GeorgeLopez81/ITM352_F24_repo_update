#Get a JSON file of data. Using a SQL-like query, select data about driver types and group.
import requests
import pandas as pd

#Create a REST query that returns the count of license by driver type
search_results= requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type").json()

#Conver the search results to a DataFrame
results_df=pd.DataFrame.from_records(search_results)
#print(results_df).head()

results_df.columns=["count", "driver_type"]
results_df= results_df.set_index("driver_type")

#print the resulting DatgaFrame
print(results_df)