# wap to print product of odd numbers from 1 to 10
i = 1

product = 1

while (i <= 10):

    if i % 2 != 0:

        product = product * i

    i += 1

print (product)