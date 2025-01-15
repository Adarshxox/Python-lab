
# 27 is a harshad number as the sum of the digits of 27 is 9 and 27 is a multiple of 9

number = 27

sum = 0

for i in str(number):

    sum += int(i)

print(sum)

if number % sum == 0:

    print(f"{number} is harshad number")

else:

    print(f"{number} is not harshad number")

