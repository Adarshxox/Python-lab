
# wap to find the factorial of a number entered by user

number = int(input("Enter the number: "))

factorial = 1

for i in range(1,number+1):

    factorial = factorial * i

print(factorial)