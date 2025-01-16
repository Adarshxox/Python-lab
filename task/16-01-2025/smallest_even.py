#  wap to find the smallest even number in the list

numbers = [12, 5, 9, 3, 14, 2, 7]

smallest_even = None

for i in numbers:

    if i % 2 == 0:  

        if smallest_even is None or i < smallest_even:

            smallest_even = i  

if smallest_even is not None:

    print("The smallest even number is:", smallest_even)
