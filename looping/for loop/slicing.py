# o/p = yhn               text str odd index element return

text = "python"

result = ""

for i in text:

    if text.index(i) % 2 != 0:

        result += i

print(result)
