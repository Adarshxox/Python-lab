# function to get the sum of digits in a number   a = 153

def sum_numbers(a):

    sum = 0

    for i in str(a):

        sum = sum + int(i)

    print(sum)

sum_numbers(153)