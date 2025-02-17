# wap to print sum of even and odd indexed digits in a given number

numbers = int(input("Enter the numbers: "))

numbers = str(numbers)

sum_of_even = 0

sum_of_odd = 0

for i in numbers:

    if numbers.index(i) % 2 == 0:

        sum_of_even += int(i)

    else:

        sum_of_odd += int(i)

print(f"sum of even indexed numbers = {sum_of_even} and odd indexed numbers = {sum_of_odd}")