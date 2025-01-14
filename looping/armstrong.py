# armstrong number
# ================

# a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits: 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.


number = int(input("Enter your Number: "))

temp = number

sum = 0

length = len(str(number))

while(number > 0):

    digit = number % 10

    sum += digit ** length

    number = number // 10

if sum == temp:

    print(f"{temp} is a armstrong number")

else:

    print(f"{temp} is not a armstrong number")
    