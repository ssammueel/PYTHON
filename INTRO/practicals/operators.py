# addition

# subtraction 
# multipication 
# divison
# modulus 
# exponiation 
x = 2
y = 5

print(x ** y) #answer 32

# floor divison 
x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number


# lists 

mylist = ["banana", "apple", "mango", "banana", "cherry", "orange", "kiwi", "melon"]
mylist2 = list(("banana", "apple", "mango", "banana")) #creating list usint the constructor list

print(type(mylist)); print(type(mylist2));
print(len(mylist)); print(len(mylist2))
print(mylist); print(mylist)

    # acessing items in a list

print(mylist[2])
print(mylist[-1])
print(mylist[1:5])
print(mylist[2:-2])
print(mylist[-5:-2])

        #inserting items 
mylist.insert(1, "cowcowfruit")
print(mylist)

    #adding item in a list
mylist.append("beatruit")
print(mylist)

    #appending items from another list
mylist.extend(mylist2)
print(mylist)

    #remove specific item
mylist.remove(banana)
print(mylist)
mylist.clear()
print(mylist)