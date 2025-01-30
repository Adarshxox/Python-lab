# fibonacci series

def fibon(n):
    
    if n == 0:

        return 0
    
    elif n == 1:

        return 1
    
    elif n > 1:

        return fibon(n - 1) + fibon(n - 2)
    
a = int(input("enter the number: "))

for i in range(a):

    print(fibon(i))