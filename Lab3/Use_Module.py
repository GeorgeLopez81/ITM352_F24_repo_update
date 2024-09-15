#Program to test the use of the HandyMath Library
#imports HandyMath.py, asks for two numbers from a user, and prints out the midpoint of those numbers,
# the square root of the square of one number, the result when raising one number to the exponent of the other,
# and finally the max and min of the numbers. Use the Python f-string capability to format these strings.
import HandyMath as HM




num1 = float(input("Enter First Value:"))
num2 = float(input("Enter Second Value:"))


mid = HM.midpoint(num1,num2)
print(f"The Midpoint Of These Two Number Is:{mid}")


sqrt = HM.sqrt(num1)
print(f"The Square Root Of The First Number Entered Is:{sqrt}")


exp = HM.exponent(num1,num2)
print(f"{exp},Is the number when the first value entered is raised to the power of the second value entered")


max = HM.max(num1,num2)
print(f"The Max/Largest Of These Two Numbers Is: {max}")


min = HM.min(num1,num2)
print(f"The Min/Smallest Of These Two Numbers Is: {min}")
