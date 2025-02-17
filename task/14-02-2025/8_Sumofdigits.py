# Write a function  that takes a positive integer n and returns the sum of its digits

def sum_of_digits(a):

    x = 0

    for i in str(a) :

        x += int(i)

    return x

n = int(input("enter the number : "))

print(sum_of_digits(n))
