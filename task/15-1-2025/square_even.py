#   wap to print the sum of sqare of even numbers of last

input = [1, 2, 3, 4, 5]

square_sum = 0

for i in input:

    if i % 2 == 0:

        square_sum += i ** 2  

print("Sum of squares of even numbers:", square_sum)
