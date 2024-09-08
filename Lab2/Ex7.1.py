#Ask the user to input a temperature in degrees Fahrenheit.
#Convert that temperature to Celsius and outpu it.

#Function to convert degrees F to degrees C
def FtoC(temperatureF)
    degreesC = (float(degreesF) - 32) * (5/9)
    return(degreesC)

degreesF = input("Enter a temperature in Fahrenheit: ")



print("This converts to " , FtoC(degreesF, "Celsius")