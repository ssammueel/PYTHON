# numbers

x =10
y = 15.5

z = 2 * x * 3 + 0.5*y

print(z)


#strings

class1  = "python prog"
print(class1)
print(len(class1))


print("enter your name");
x = input()
print("hello, " + x)

#strings
print("enter name")
x = input()
print("hello, " + x)


print("enter the first name")
firstName = input()
print("enter the last name")
lastName = input()
print("your full name is ," + firstName + " " + lastName)

#using math lib
from math import sin,  cos
x = 3.14
y = sin(x)
print(y)
y = cos(x)
print(y)


#using matplotlib
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,2,4,4,8,7,10,9,10,3]

plt.plot(x, y)
plt.xlabel("time (s)")
plt.ylabel("Temperature (degC)")
plt.show()