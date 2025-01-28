# to check sum of 3 different numbers is odd or even

def sum():

    sum = 0

    a = int(input("enter the first number: "))  
    
    b = int(input("Enter the second12 number: "))

    c = int(input("Enter the third number: "))

    sum = a + b + c

    if sum % 2 == 0:

        print(f"Sum of the three numbers is even: {sum}")

    else:

        print(f"Sum of the three numbers is odd: {sum}")

sum()

