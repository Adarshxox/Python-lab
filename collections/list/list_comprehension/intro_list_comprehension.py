# list comprehension is to simplyfy the exixting program. we can reduse the line of codes

numbers = [1,2,3,4,5,6]

# even = []

# for i in numbers:

#     if i % 2 == 0:

#         even.append(i)

# print(even)

result = [i for i in numbers if i % 2 == 0]

print(result)