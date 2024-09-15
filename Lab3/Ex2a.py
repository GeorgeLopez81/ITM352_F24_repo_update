#midpoint that takes two numbers as input and returns the value halfway between them
def midpoint(num1, num2):
    return((num1 + num2)/2)
number1 = float(input("Enter First Value:"))
number2 = float(input("Enter Second Value:"))


mid = midpoint(number1, number2)


print("The midpoint is:", mid)