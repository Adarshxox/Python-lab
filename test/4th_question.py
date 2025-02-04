"""""
Write a program to check if the given number is a Disarium Number
A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes 
equal to the number itself.
For example, 175 is a Disarium number as follows:
11+ 72 + 53 = 1+ 49 + 125 = 175

"""
num = int(input("enter the number: "))

num_str = str(num)

disarium_number = 0

for i in range(len(str(num))):

    disarium_number += int(num_str[i]) ** (i + 1)

if disarium_number == num :

    print(f"{num} is disarium number")

else:

    print(f"{num} is not disarium number")
