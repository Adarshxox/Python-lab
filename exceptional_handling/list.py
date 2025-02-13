# wap to enter a list of numbers

#1) convert all the type of numbers in list to int

#2) try to pick a element from a specific index

numbers = [1,2,"3",4,"abc"]

new = []

try:

    for i in numbers:

        i = int(i)

        new.append(i)

except ValueError:

    print("Please enter the correct value!!!!!")