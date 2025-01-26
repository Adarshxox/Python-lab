#  text = "programming"                                          #{"p":1,"r":2,"o":1,"g":2,"a":1,"m":2,"i":1,"n":1}


text = input("Enter your word: ")

# result = {}

# for i in text:

#     result[i] = text.count(i)

# print(result)


# without using count

new = " "

for i in text:

    count = 1

    if i in new:

        count = count + 1

    new =new + i

    print(i,count)
    