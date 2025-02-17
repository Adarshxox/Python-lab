# Write a function  that reverses the order of words in a given sentence but keeps the characters in each word in the correct order.
# Example: "Hello World" → "World Hello"

def reverse(sentance):

    rev_sentence = " "

    for i in sentance.split(" ")[::-1]:

        rev_sentence = rev_sentence + i + " "

    return(rev_sentence)

text = input("enter the sentance: ")

print(reverse(text))