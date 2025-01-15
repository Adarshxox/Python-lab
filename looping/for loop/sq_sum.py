
# find the sum of square of n natural numbers.

# n is entered by user

n = int(input("Enter the number: "))

sum = 0

for i in range(1,n+1):

    sum = sum + i **2

print(sum)

