#First, super simple use of matplotlib
import matplotlib.pyplot as plt  #pie plot

x_values=[1,2,3,4,5]
y_values=[1,3,3,3.5,4]

#Plot these values
#plt.plot(x_values, y_values)
plt.scatter(x_values, y_values)

other_x=[1,2,3,4]
other_y=[2,4,6,8]
plt.plot(other_x,other_y)

plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Line and Scatter Plot")


plt.show()
