# wap to print the numbers divisible by 3 from 1 to n

n = int(input("enter the number: "))

for i in range(1, n+1):

    if i % 3 == 0:

        print(i)

    