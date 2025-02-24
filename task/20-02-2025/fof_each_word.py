# write a program that take a string as input and counts the frequecy of each word in the string

# text = "Hello world! Hello python. python is great, isn't it?"

# word freequencies

"""""
Hello : 2
world : 1
python: 2
is : 1
great : 1
isn't : 1
it : 1

"""

text = "Hello world! Hello python. python is great, isn't it?"

text = text.lower()

clean_text = ""

for i in text:

    if i not in "!,.?:":

        clean_text += i

    else:

        clean_text += " "  # Replace punctuation with space to separate words

words = clean_text.split()

word_count = {}

for i in words:

    if i in word_count:

        word_count[i] += 1

    else:

        word_count[i] = 1

for word, count in word_count.items():

    print(f"{word} : {count}")