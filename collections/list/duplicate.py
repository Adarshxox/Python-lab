# wap to find the duplicate element in the list

elements = [6,4,2,3,1,3,5,7]

for i in elements:

    if elements.count(i) > 1:

        print(i)

        break
