myList = [1,2,"abc", (1,2,3), True, ["a",2,3],10, 20, 33, "howdy", False]

if (len(myList) < 5):
    print("Less than 5 elements")
elif(5 <= len(myList)<=10):
    print("Between 5 and 10 elements")
else:
    print("Greater than 10 elements")