
with open("Names.txt", mode="r") as textFile:
    NameList = textFile.read()
    print(type(NameList))
    print(NameList)

SeperatedList = NameList.split("\n")
print(SeperatedList)
count=len(SeperatedList)
print(f"There are {count} names in the file")



