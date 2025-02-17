# Write a function that returns a list of all divisors of n.

def divisor(n):

    temp_list = []

    for i in range(1,n+1):

        if n % i == 0:

            temp_list.append(i)

    return(temp_list)

div = int(input("enter the number : "))

print(divisor(div))