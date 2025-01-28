text = "regulate"

word = input("enter the word: ")

# kangaroo >> chars should be in the source word

w_count = {}

for i in text:

    w_count[i] = text.count(i)

print(w_count)

for j in word:

    if j in w_count and w_count[j] > 0:

        w_count[j] -= 1

    else:

        print("Not kangaroo")

        break

else:

    print("Is a Kangaroo")
