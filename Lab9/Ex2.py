import csv

line_number = 0
total_RealInc = 0
num_values = 0
max_RealInc = -float('inf')  
min_RealInc = float('inf')   


with open("/Users/georgelopez/Downloads/survey_1000.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for line in csv_reader:
        if line_number > 0:  
            if len(line) > 5456:  
                try:
                    RealInc = float(line[5456])  
                    if RealInc > 0:  
                        num_values += 1
                        total_RealInc += RealInc

                        
                        if RealInc > max_RealInc:
                            max_RealInc = RealInc  

                        if RealInc < min_RealInc:
                            min_RealInc = RealInc  

                except ValueError:
                    pass  
        line_number += 1


if num_values > 0:
    print(f"Number of non-zero values: {num_values}")
    print(f"Average RealInc: ${round(total_RealInc / num_values, 2)}")
    print(f"Min RealInc: ${min_RealInc} Max RealInc: ${round(max_RealInc,2)}")
else:
    print("No valid RealInc data found.")
