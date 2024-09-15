#midpoint that takes two numbers as input and returns the value halfway between them
def midpoint(num1, num2):
    return((num1 + num2)/2)
number1 = float(input("Enter First Value:"))
number2 = float(input("Enter Second Value:"))


mid = midpoint(number1, number2)


print("The midpoint is:", mid)

#Creates a function called "sqrt" that takes a number
#and returns the squareroot of that number. Use the fact that the square root of n is n**0.5.


def sqrt(num):
    return((num**0.5))


numinput = float(input("Enter A Number: "))

# Program that takes two numbers, a base and an exponent,
# and returns the value when you raise the base to the power of the exponent


def exponent(base, exponent):
    return((base)**exponent)


base = float(input("Enter Base:"))
exp = float(input("Enter Exponent:"))


expo = exponent(base, exp)


print("The Number You Entered As A Base Was: ", base)
print("The Number You Entered As An Exponent Was: ", exp)
print("The Number Entered Is:",expo)


numsqrt = sqrt(numinput)


print("The Number You Entered Was: ",numinput)
print("The Number when Square Rooted Is:",numsqrt)

#Program that takes two numbers as input and returns the value of the larger one


def max(a, b):
    return (a + b + abs(a - b))/2


num1 = float(input("Enter First Value:"))
num2 = float(input("Enter Second Value:"))


bigger = max(num1, num2)


print("The max in this number set is:", bigger)

#Program that takes two numbers as input and returns the value of the larger one


def min(a, b):
    return (a + b - abs(a - b))/2


num1 = float(input("Enter First Value:"))
num2 = float(input("Enter Second Value:"))


smaller = min(num1, num2)


print("The min in this number set is:", smaller)