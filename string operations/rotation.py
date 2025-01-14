# text = "python"

# # o/p = "npytho"

# result = text[-1] + text[0:-1]

# print(result)

text = "hellopython"

# o/p = "ollehpython"

if "p" in text:

    item = text[0 : text.index("p")]  # text [0:5]

    print(item[:: -1] + text[text.index("p")::])

    # print ("olleh" + text[5::])
    # print ("olleh" + "python")
    # ollehpython

else:

    print("Thank You")

