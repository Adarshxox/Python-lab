items = {2:8,4:6,7:9,1:2}

#  [10,10,16,3]

# result = []

# for i in items:

#     n = 0

#     n = i + items[i]

#     result.append(n)

# print(result)

print([i+items[i] for i in items])

