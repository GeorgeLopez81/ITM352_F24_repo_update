# Create a scatter plot of fares and distances
import matplotlib.pyplot as plt
import pandas as pd

trips_df=pd.read_json("../Trips from area 8.json")

trip_miles_gt_o = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')#when analyzing the data ingnore the "0"
fare_series = trip_miles_gt_o.to_fare
trip_miles= trip_miles_gt_o.trip_miles
#use trianagles to make the visualization better
#plt.plot(fare_series, trip_miles, linestyle="none", marker=".")
plt.plot(fare_series, trip_miles, marker="v", linestyle="none", color='c', alpha=0.2)
#plt.scatter(fare_series, trip_miles)
plt.title("Fares by Taxi Trip Miles")
plt.ylabel("Distance in Miles")
plt.xlabel("Total Fare in Dollars")

plt.savefig("FaresXMiles.png", dpi=300)#creates a file
plt.show()
