
Weird = ("hello", 10, "goodby", 3, "goodnight", 5, "goaway")

userVal = input("Please enter a value: ")
try:
   
    Weird[7] = userVal
except:
    
    print("You cannot add elements to a tuple, doofus!")
    Weird = Weird + (userVal,)

print(f"Updated tuple: {Weird}")
