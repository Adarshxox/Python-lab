# wap to print the repeated elements

text = "welcome"

i = 0

while(i < len(text)):

    if text.count(text[i]) > 1:   # text.count(elements)

        print(text[i])

    i += 1

