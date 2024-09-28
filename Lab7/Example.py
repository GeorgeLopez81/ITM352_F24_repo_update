#Program to cunt letter frequencies in a string



#Count the frequency of letters in an input string, ignoring case
def getFrequencies(inString):
    feqDict = {}
    for character in inString:
        character= character.lower()
        if character not in freqDict:
            freqDict[character]= 1

        else:
            feqDict[character]+=1 1
            return freqDict
        
inputString = input("Please enter a string; ")

dict = getFrequencies