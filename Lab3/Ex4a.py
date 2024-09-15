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