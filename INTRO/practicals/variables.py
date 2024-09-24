print("samuel")

#comments begin with #

'''
samuel
this is 
mulltiline comment
'''
#variables
# -> there is no command for creating variables they are created the moment a value is assignesd to it

x = 10
print(x)
#see the type
print(type(x))  #prints <class 'int'>

# you can specify type 
y = str(10)  #print 10
w = float(10) #print 10.0
u = int(10) # print 10

#assigning multiple variables in a line

a,b,c = 10,20,30
print(a); print(type(a));
print(b); print(type(b));
print(c); print(type(c))

letters = 10,20,30
a,b,c = letters
print(a); print(type(a));
print(b); print(type(b));
print(c); print(type(c))

#variables created outside a fuction are known as global variables
# to create a global function inside a variable we use the keyword global

def read():
    global x;
    f = 10
read()

# function ends when indentation ends