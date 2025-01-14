
number = input("Enter a number: ")


product = 1


for digit in number:

    product *= int(digit)


print("The product of the digits is:", product)
