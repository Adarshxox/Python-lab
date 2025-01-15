# wap to print even numbers from 1 to n

# n entered by user

n = int(input("enter the number: "))

for i in range(1,n+1):

    if i % 2 == 0:

        print(i)

