# wap to find the greatest odd number from the list

numbers = [12, 5, 9, 3, 14, 2, 7]

greatest_odd = None

for i in numbers:

    if i % 2 != 0:  

        if greatest_odd is None or i > greatest_odd:

            greatest_odd = i  


if greatest_odd is not None:
    
    print("The greatest odd number is:", greatest_odd)
else:
    print("There is no odd number in the list.")
