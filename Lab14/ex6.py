 # Create a scatter plot of fares and distances
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

trips_df=pd.read_json("../Trips from area 8.json")
#have to choose the miles that I need
trips_gt_1 =trips_df[['trip_miles', ,'fare', 'dropoff_community_area' ]].query('trip_miles > 1')

fare_series= trips_gt_1.fare 
trip_miles = trips_gt_1.trip_miles
dropoff_area= trips_gt_1.dropoff_community_area

fig=plt.figure()
ax= fig.add_subplot(111, projection='3d')

#Put fare series on the xaxis, dropoff area on the axis, miles on they y axis
ax.scatter(fare_series, trip_miles, dropoff_area, c= 'b', marker='.')

plt.title()