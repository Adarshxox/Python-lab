# wap to print the characters of a string in even positions. >>>      name= "python"    o/p = y h n


text = "python"

for i in text:

    if text.index(i) % 2 != 0:

        print(i,end=" ")