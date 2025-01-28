# find armstrong number

def armstrong_num(a):

    length = len(str(a))

    sum = 0

    temp = a

    while a> 0:

        dig = a % 10 

        sum += (dig ** length)

        a = a // 10

    print(f"{temp} = {sum}")

    if temp == sum:

        print(f"{temp} is armstrong number")

    else:

        print(f"{temp} is not armstrong number")

armstrong_num(153)


# using for loop

def is_armstrong(num1):

    length = len(str(num1))

    sum = 0

    for i in str(num1):

        sum = sum + int(i)**length

    print("armstrong" if sum == num1 else "not armstrong")

is_armstrong(153)

is_armstrong(23)