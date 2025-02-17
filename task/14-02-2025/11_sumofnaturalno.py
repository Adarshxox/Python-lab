#  Write a function  that returns the sum of the first n natural numbers using the formula:
#    Sum = n(n+1)/2


def sum_of_nat_no(x):

    return (x * (x + 1)) /2
    
n = int(input("enter a natural number : "))

print(sum_of_nat_no(n))