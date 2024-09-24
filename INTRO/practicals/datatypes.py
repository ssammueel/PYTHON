# printing random number
import random

print(random.randint(1, 10))

#print string 
a = "samuel is a name a boy"
print(a[4])     #prints e

#check certain text n sentence
print("name" in a) #print true 
print("samuel" not in a) #false

if "name" in a:
    print("the text was found thanks to you samuel")

#print characters in a range
name = "there is a place"
print(name[3:9])    #prints letters from 3 to 9
print(name[-5:-2]) #prints pla

print(name.upper())
print(name.lower())
print(name.strip()) #removes white spaces

print(name.capitalize())    #capitilizes the first letter alone

# splits the string into substrings if it finds instances of the separator
print(name.split(" "))