
Weird = ("hello", 10, "goodby", 3, "goodnight", 5, "goaway")
userVal = input("Please enter a value: ")

try:
    # This will have an error because tuples are immutable
    Weird[7] = userVal
except:
    print("You cannot add elements to a tuple, doofus!")
    
    # Recast tuple to a list, append the value, then cast back to tuple
    Weird_list = list(Weird)  
    Weird_list.append(userVal)  
    Weird = tuple(Weird_list)  

print(f"Updated tuple: {Weird}")
