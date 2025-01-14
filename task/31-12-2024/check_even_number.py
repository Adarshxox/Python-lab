# Check the even numbers


a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

# 1. Check if both numbers are even


if a % 2 == 0 and b % 2 == 0:

    print("Both numbers are even.")

else:

    print("Both numbers are not even.")

# 2. Check if either number is even


if a % 2 == 0 or b % 2 == 0:

    print("Either a or b is even.")

else:

    print("Neither a nor b is even.")
