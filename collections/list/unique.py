# wap to find the repeating elements and display the one element

numbers = [1,8,2,3,7,5,1,10,2]

unique = []

for i in numbers:

    if i not in unique:

        unique.append(i)

unique.sort()

print(unique)

