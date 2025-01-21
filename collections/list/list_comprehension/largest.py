# wap to find largest word without repeating any characters

text = "python is a programming language"

largest = ""

for i in text.split(" "):

    for j in i :

        if i.count(j) > 1:

            break

    else:
        
        if len(i) > len(largest):

            largest = i

print(largest)

