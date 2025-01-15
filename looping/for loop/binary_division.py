# wap to print binay number

number = int(input("Enter the number: "))

result =""

while(number>0):

    solution = number // 2

    rem = number % 2

    result = str(rem) + result

    number = number // 2

print(result)

