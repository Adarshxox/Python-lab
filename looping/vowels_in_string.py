# wap to find the count of vowels in string 

"""to find how many elements in the string"""

text = "hellopython"

i = 0

count = 0

while(i < len(text)):

    if text[i] in "aeiou":

        count = count + 1

    i = i + 1

print(f"the count of vowels in string is {count}")

"""how many strings and which are they specifically"""

text = "hellopython"

a = ""

i = 0

while(i < len(text)):

    if text[i] in "aeiou" and text[i] not in a :

        print(f"{text[i]} is a vowel and it has a count of {text.count(text[i])}")

        a = a + text[i]

    i += 1

