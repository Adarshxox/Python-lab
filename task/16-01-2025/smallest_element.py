# wap to find the smallest element in the list


number = [12, 5, 9, 3, 14, 2]

smallest = number[0]

for i in number:

    if i < smallest:

        smallest = i


print("The smallest element is:", smallest)
