# wap to identify the most recursive element in the list

elements = [1,2,3,4,2,6,7,1,2,8,9,2,4,3]

max_count = 0

for i in elements:

    count = elements.count(i)

    if count > max_count:

        max_count = count

print(f"count is {count} and maximum count {max_count}")

