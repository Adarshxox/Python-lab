# find harshad number

def harshad(a):

    temp = a 

    sum = 0
     
    while a > 0:
        
        dig = a % 10

        a = a // 10

        sum += dig

    if temp % sum == 0:

        print("Harshad Number")

    else:

        print("Not Harshad number")

harshad(27)

# using for loop

def is_harshad(num):

    sum = 0

    for i in str(num):

        sum+= int(i)

    if num % sum == 0 :

        print("harshad")

    else:

        print("not harshad")

is_harshad(23)
