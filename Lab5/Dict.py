#Creat a dictionary

capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}


#Print the dictionary
print(capitals)
print(capitals["Germany"])
print(capitals["England"])

del capitals["Germany"]
print("After delete: ", capitals)

capitals["Italy"]= "Rome"
capitals["Italy"]= "Naples"

print("After add: ", capitals)

print("Length of capitals=", len(capitals))

#capitals.clear()

#print("After clear", capitals)

print("Candada" in capitals)
print("Germany" in capitals)


