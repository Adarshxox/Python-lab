items = {"a":1,"b":2,"c":3}          # {1:"a",2:"b",3:"c"}

result = {}

for i in items:

    result[items[i]] = i             # result[1] = a

print(result)


items = [1,2,2,3,3,3,4,4,4,4]        # {1:1,2:2,3:3,4:4}

result = {}

for i in items:

    result[i] = items.count(i)

print(result)
