# IF...ELSE
a = 5

b = 10
if a > b:
    print("a is greater than b")
if b > a:
    print("b is greater than a")
if a == b:
    print("a is equal to b")


            #  using user input 
a = input("Enter the value of A:")

b = input("Enter the value of B:")
if a > b:
    print("a is greater than b")
if b > a:
    print("b is greater than a")
if a == b:
    print("a is equal to b")



# ELIF
a = 5
b = 10

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")



#ELSE IF
a = int(input("enter marks, "))
if a > 50:
    print("pass")
else:
    print("fail")



# FOR LOOP
for i in range(1, 10):
    print(i)


# printing even numbers
for i in range(1, 15):
    if i % 2 == 0:
        print(i)


#for loop with user input
data1 = int(input("enter the first number, "))
data2 = int(input("enter the last number, "))

data = [data1, data2]
print(data)

sum = 0

for x in data:
    sum = sum + x
print(sum)

n = len(data)
mean = sum/n
print(mean)