"""""
Make a dictionary of student name  and their scores. (5 elements)


>> find the highest score

>> find the smallest score

"""

scores = {"aju":77, "babu":64, "cibi":56, "danny":84, "eldho":45}

highest = 0

smallest = 100

for i in scores:

    smallest = min(smallest,scores[i])

    highest = max(highest,scores[i])

print(highest)

print(smallest)

