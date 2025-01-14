# a positive integer that is eqaul to sum of its proper divisors, which are all of its divisors excluding the number itself
# =========================================================================================================================

# 6 = 1, 2, 3

# 28 = 1, 2, 4, 7, 14

num = int(input("enter the number: "))

i = 1

sum = 0

while(i < num):

    if num % i == 0:

        print(i)

        sum = sum + i

    i += 1

if sum == num:

    print(f"{num} is a perfect number")

else:

    print(f"{num} is not a perfect number")

