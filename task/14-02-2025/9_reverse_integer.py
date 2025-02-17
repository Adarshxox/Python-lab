# Write a function  that takes an integer n and returns its reverse.
# Example: reverse_integer(1234) should return 4321. 

def reverse_integer(x):

    x = str(x)

    return(x[::-1])

n = int(input("enter the number : "))

print(reverse_integer(n))