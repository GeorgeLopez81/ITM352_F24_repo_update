#Ask the user to enter their first name, middle initial and last name. Concatenat them
# together with spaces in between and print out the result.

First = input("Please enter your first name: ")
MiddleInitial = input("Please enter your middle initial: ")
Last = input("Please enter your last name: ")

FullName = First + " " + MiddleInitial + " " + Last
print("Your full name is" , FullName)
print(f"Your full name is {First} {MiddleInitial} {Last}") #differnt way of putting strings together

print("Your full name is %s %s %s" % (First, MiddleInitial, Last))


# Creating a list with the user's full name components
FullName = [First, MiddleInitial, Last]

# Using the format method to concatenate and format the full name
formatted_name = "{} {} {}".format(FullName[0], FullName[1], FullName[2])

# Printing the full name using the format() method
print("Your full name is: " + formatted_name)


# Creating a list with the user's full name components
FullName = [First, MiddleInitial, Last]

# Using the join() method to concatenate the full name
joined_name = " ".join(FullName)

# Printing the full name using the join() method
print("Your full name is: " + joined_name)


# Taking user input for first name, middle initial, and last name
First = input("Please enter your first name: ")
MiddleInitial = input("Please enter your middle initial: ")
Last = input("Please enter your last name: ")

# Creating a list with the user's full name components
FullName = [First, MiddleInitial, Last]

# Using the format() method with list unpacking
formatted_name = "{} {} {}".format(*FullName)

# Printing the full name using the format() method
print("Your full name is: " + formatted_name)
