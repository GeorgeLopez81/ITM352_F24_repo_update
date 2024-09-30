# Create a list of elements containing the odd numbers between 1 and 50

oddNumbers = []
# a.	Use range() and an if-statement in a “traditional” for loop
for num in range(1,50):
 
   if num % 2 == 1:
        oddNumbers.append(num)

#b.	Use range() and the fact an odd number is 2*num + 1
for num in range(0,25):
   oddNumbers.append(2 * num+1)


# c.	Use range() with a step and no if-statement or use 2*num + 1
for num in range(1,50,2):
    oddNumbers.append(num)

# d.list comprehension
oddNumbers = [x for x in range(1,50) if x % 2 != 0]



print(oddNumbers)