#Creates a function called "sqrt" that takes a number
#and returns the squareroot of that number. Use the fact that the square root of n is n**0.5.


def sqrt(num):
    return((num**0.5))


numinput = float(input("Enter A Number: "))


numsqrt = sqrt(numinput)


print("The Number You Entered Was: ",numinput)
print("The Number when Square Rooted Is:",numsqrt)