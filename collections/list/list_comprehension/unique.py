# text = "abcbcdedf"

# print([i for i in text if text.count(i) == 1])

# unique = []

# for i in text:

#     if text.count(i) == 1:

#         unique.append(i)

# print(unique)

text = "pythonlanguage"

result = [i for i in text if i not in "aeiou"]

# unique = [i for i in result if result.count(i) == 1 ]

unique = []

for i in result:

    if i not in unique:

        unique.append(i)

print(unique)