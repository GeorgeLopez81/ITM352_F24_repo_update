#append an input from the user to the tuple that you created in
#  Exercise 3 and print out the appended tuple.
Weird = ("hello", 10, "goodby",3, "goodnight",5, "goaway")

userVal = ("please enter a value: ")

try:
   Weird[7] = (userVal)

except:
  print("You can not add elements to a tuple doofus!")