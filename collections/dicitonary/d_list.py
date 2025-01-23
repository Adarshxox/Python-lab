person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "rating": 1550,
    "nationality": "Indian"
}

# item1 = ["name","age","city","rating","nationality"]
# ====================================================

# item2 = ["john",25,"New York",1550,"Indian"]
# ============================================

# item1 = []

# item2 = []

# for i in person:

#     item1.append(i)

#     item2.append(person[i])

# print(item1)

# print(item2)

print([i for i in person])

print([person[i] for i in person])