#Debugging exercise # 6
# Write code that will iterate through numbers from 1 to 10 and print the number if 
# it is not equal to 5 (using continue) and stop the loop entirely and print a message 
# when it reaches 8 (using break).


for x in range(1, 11):  
    if x == 5:
        continue  
    if x == 8:
        print("done!")
        break
    print(x) 