# second largest without using any methods

numbers = [97,88,4,7,12,45,81,25]

largest = numbers[0]

second_largest = numbers[1]

for i in numbers:

    if i > largest :

        second_largest = largest

        largest = i

    elif i > second_largest and i < largest:

        second_largest = i

print(f"{second_largest} is the second largest number.")
