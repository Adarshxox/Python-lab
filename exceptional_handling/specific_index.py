# wap to enter a list of numbers

# try to pick a element from a specific index

numbers = [1,2,3,4,5]

try:

    index = int(input("enter the index number:"))

    print(numbers[index])

except IndexError:

    print("Index is out of range....")

except ValueError:

    print("Enter the correct value.....")
