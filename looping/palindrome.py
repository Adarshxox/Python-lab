"""

a number that remains the same when its digits are reserved.


for example, 121, 1331, and 4554 are all palindrome

"""

# number = int(input("Enter the number: "))

number = 121

temp = number

rev = 0

while(number > 0):

    digit = number % 10

    rev = rev * 10 + digit

    number = number // 10

# print(rev)

if rev == temp:

    print(f"{rev} is a palindrome")

else:

    print(f"{rev} is not a palindrome")

