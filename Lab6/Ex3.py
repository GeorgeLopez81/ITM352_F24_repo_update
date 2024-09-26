
year = int(input("Enter a year: "))


is_leap_year = "leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "not a leap year"


print(is_leap_year)
