
items = {"a":1,"b":2,"c":1,"d":3,"e":2}                           # remove keys with duplicate values

result = []

for i in items.copy():                                            # "a"

    if items[i] in result:                                        # if 1 in result True

        items.pop(i)                                              # items to pop

    elif items[i] not in result:                                  # if items is false

        result.append(items[i])                                   # append to end of list

print(items)