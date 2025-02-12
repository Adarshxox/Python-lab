file =open("new_t.txt","r")

elements =[]

details = {}

avg = 0

for i in file.readlines():

    elements = i.strip().split()

    if len(elements) < 1 :

        continue

    else:

        name = elements[0]

        mark = list(map(int,elements[1:]))

        avg = sum(mark)/len(elements)

        elements.append({"name" : name, "average": avg})

print(elements)