import csv

#  variables
line_number = 0
total_fare = 0
num_fares = 0
max_trip_miles = -float('inf')  

with open("/Users/georgelopez/Downloads/taxi_1000.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for line in csv_reader:
        if line_number > 0:
            try:
                fare = float(line[9])  
                trip_miles = float(line[7])  

                total_fare += fare
                num_fares += 1

                if trip_miles > max_trip_miles:
                    max_trip_miles = trip_miles

            except ValueError:
                pass  
        line_number += 1

if num_fares > 0:
    average_fare = round(total_fare / num_fares, 2)
    print(f"Number of fares: {num_fares}")
    print(f"Total Fare: ${total_fare}")
    print(f"Average Fare: ${average_fare}")
    print(f"Max Trip Miles: {max_trip_miles}")
else:
    print("No valid fare data found.")