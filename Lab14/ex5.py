# Create a scatter plot of fares and distances
import matplotlib.pyplot as plt
import pandas as pd

#Use different plot styles
#plt.style.use('ggplot')
#plt.style.use("fivethirtyeight")
plt.style.use("dark_background")

trips_df=pd.read_json("../Trips from area 8.json")
trip_miles_gt_o = trips_df[['trip_miles', 'fare']].query('trip_miles > 2')

fare_series = trip_miles_gt_o.to_fare
trip_miles= trip_miles_gt_o.trip_miles

plt.plot(fare_series, trip_miles, marker="0", linestyle="none", alpha=0.3)
plt.title("Fare by Taxi Trip Miles >2")
plt.xlabel("Fare")
plt.ylabel("Distance in Miles")

plt.legend()

plt.savefig("FaresXMiles.2.png", dpi=300)#creates a file
plt.show()