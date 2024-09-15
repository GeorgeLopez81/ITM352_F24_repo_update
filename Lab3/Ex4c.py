#Program that takes two numbers as input and returns the value of the larger one


def min(a, b):
    return (a + b - abs(a - b))/2


num1 = float(input("Enter First Value:"))
num2 = float(input("Enter Second Value:"))


smaller = min(num1, num2)


print("The min in this number set is:", smaller)