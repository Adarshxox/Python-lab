# file handling in python involves operations such as creating, reading, writing,and closing files, uitilising various modes to manage data

"""""
FILE OPERATIONS
===============

read()            'r'

write()           'w'

append()          'a'


open("filename","mode")
file.read()
file.close()

"""

# file = open("sample.txt","r")

# print(file.read())

# file = open("new.txt","w")    # if the file is not exist a new file will create / if there is an existing file it will overwrite

# file.write("Hello")

# append

# file = open("sample.txt","a")

# file.write(str(list(range(1,10))))

# items = [1,True,"hello",5.6]

# file = open("data.txt","w")

# for i in items :

#     file.write(str(i))


# file = open("new.txt","r")      # Python is a Programming Language

# result = file.read()

# print(result)                   # Python is a Programming Language

# print(len(result.split(" ")))   # 5

# file = open("new.txt","r")

# result = file.read().split()

# n = input("enter the word: ")

# print(result.count(n))

# if n not in result:

#     print("Not Exist")

# python is a popular programming language python is used to create web applications

# ["python","is","a","popular","rogramming","language","used","to","create","web","applications"]

# file = open("new.txt","r")

# print(list(set(file.read().split(" "))))

# file = open("C:/Users/Aadhu/Desktop/Python Labs/collections/list/list comprehension/task.txt","w")

# file.write("python is a language")

# file = open("new.txt","r")

# print(file.readline())    # only read the first line in the content

# print(file.readlines())   # each line represent as a element in a list

# print(file.readable())    # to find the conte is readable or not

# with open("new.txt","r") as file:

#     print(file.read())   

# file.close()  | with >> it ensures closing files right after processing them. it will close automatically after the command

# copy contents from one file to another file in python

# with open("new.txt","r") as first , open("data.txt","r") as second:

#     print(first.read()and second.read())

# file = open("new.txt","r")

# result = file.read()

# file.close()

# file = open("new_t.txt","w")

# file.write(result)


file = open("new_t.txt","r+")   #read and write

result = file.read()

file.write("hello world")
