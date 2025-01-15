
# prime numbers    (2,3,5,7,11,13,...........)

number = int(input("enter the number: "))

if number > 1:

    for i in range(2,number):

        if number % i == 0:

            print(f"{number} is not prime number")

            break

    else:

        print(f"{number} is a prime number.")
        
else:

    print("enter the number greater than one")