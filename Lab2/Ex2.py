#Get the users birth year and subtract the current year to 
#get thier current age.

birth_year = input("Please enter your four digit birth year: ")
birth_year = int(birth_year)
current_year = 2024  #This should be changed. We should not hare-code the year
age = current_year - birth_year  #This doesnt take into accound the number of months. Need to fix
print("You entered: ", birth_year)
print("your age is: " , age)
