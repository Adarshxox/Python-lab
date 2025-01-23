text = "Mysql is a working database"

words = text.split(" ")

for i in words:

    for j in i:

        if j in "aeiou":

            break

    else:

        print(i)
        