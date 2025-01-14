# wap to find the divisors of the number enter by user

num = int(input("enter the number: "))

i = 1

while(i < num):

    if num % i == 0:

        print(i)

    i = i + 1

