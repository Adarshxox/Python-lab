import re

# text = "Hello python"

# pattern = "python"

# if re.match(pattern,text):            # re.match will only check the begining of the text

#     print("Match Found")

# else:

#     print("No Match Found")

#         01234567890123456789012345678901
# text = "python is a programming language"

# pattern = "program"

# if re.search(pattern,text):             # checks the pattern matches anywhere in the string

#     print("Match Found")

# else:

#     print("No Match Found")

# result = re.search(pattern,text)          # checks the pattern matches anywhere in the string

# if result:

#     print(result.group())

#     print(result.start())

#     print(result.end())

# text = "python is a programming language python used to build backend"

# pattern = "python"

# match = re.findall(pattern,text)            # find all pattern occurrence in a string

# print(match)

text = "python is a programming language python used to build backend"

pattern = "python"

match = re.finditer(pattern,text)

for i in match:

    print(i.group())

    print(i.start())

    print(i.end())