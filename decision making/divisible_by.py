
# Enter the number by user

# check wheather number is divisible by both 2 and 3 print "divisible by both"  eg: 6

# check  number is divisible by 2 not by 3 >> divisible by only 2   eg: 4

# check number is divisible by  either 2 or 3 >> (either 2 or 3)   eg: 68

# check number is not divisible by both 2 and 3 >>(not divisible by both)   eg: 5

number = int(input("Enter the number: "))

if number % 2 == 0 and number % 3 == 0:

    print(f"{number} is divisible by both")

elif number % 2 == 0 and number % 3 != 0:

    print(f"{number} is divisible by Only 2")

elif number % 2 == 0 and number % 3 == 0:

    print(f"{number}either by 2 or 3")

elif number % 2 != 0 and number % 3 != 0:

    print(f"{number} is not divisible by both")

