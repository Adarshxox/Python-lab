# write a function longest_word(sentence) to find and return the longest word in a sentence

def longest(text):

    longest = 0

    for i in text.split(" "):

        if len(i) > longest:

            longest = len(i)

            new = i

    print(new)

longest("Python is a programming language")