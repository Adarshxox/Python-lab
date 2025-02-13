# exceptional handling / error handling
# =====================================
"""""
handles errors that occurs during the execution of a program.
allows to respond to the error, instead of crashing the running program.
it enables you to catch and manage errors, making your code more robust and user-friendly.

"""


# division
try:

    a = int(input("enter the first number: "))

    b = int(input("enter the second number: "))

    result = a/b

    print(result)

except ZeroDivisionError:

    print("division by zero is not possible")

except ValueError:

    print("enter a valid number: ")
    