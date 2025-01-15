# wap to print the count of vowels from a string

text = str(input("enter the string: "))         # hellopython

count = 0

for i in text:

    if i in "aeiou":

        count = count + 1

print(count)