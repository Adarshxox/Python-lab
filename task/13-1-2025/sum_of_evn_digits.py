
number = input("Enter a number: ")


sum_of_even = 0


for digit in number:

    if int(digit) % 2 == 0:
        
        sum_of_even += int(digit)


print("The sum of the even digits is:", sum_of_even)
