
number = input("Enter a number: ")


sum_of_even = 0


for i in number:

    if int(i) % 2 == 0:
        
        sum_of_even += int(i)


print("The sum of the even digits is:", sum_of_even)
