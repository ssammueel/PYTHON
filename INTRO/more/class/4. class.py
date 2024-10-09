a, b = 0, 1

for _ in range(10):
    print(a)
    temp = a
    a = b
    b = temp + b


print("Prime numbers between 2 and 50:")
for num in range(2, 51):
    prime = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = 0
    if prime == 1:
        print(num)





num = int(input("enter num 1 ,"))

if num%2 == 0:

    if num%3 ==0:
        print("divisible by 3 and 2")
    else:
        print("divisible by 2 and not by 3")
else:
    if num%3 == 0:
        print("divisible by 3 and not by 2")
    else:
        print("not divisible by 2 not dvisible by 3")








amount = int(input("enter amount: "))

if amount < 1000:
    discount = amount * 0.05;
    print("discount ", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("discount ", discount)
else:
    discount = amount * 0.15
    print("discount" , discount);
print("net payable: ", amount - discount)