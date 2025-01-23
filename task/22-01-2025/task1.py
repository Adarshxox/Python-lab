keys = ["orange","apple","kiwi","grape"]

values= ["hello","hai"]

result = {}

for i in range(len(keys)):

    if i < len(values):

        result[keys[i]] = values[i]  # values from the list

    else:

        result[keys[i]] = i - len(values) + 1  # Assign numeric values in values

print(result)

#    {"orange": "hello","apple":"hai","kiwi":1,"grape":2}

