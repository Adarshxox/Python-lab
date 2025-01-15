#  wap to find sum of digit in a number

number = int(input("enter your number: "))

sum = 0

for i in str(number):

    sum += int(i)

print(sum)