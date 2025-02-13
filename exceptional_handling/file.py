# wap to read file and read the content. It should handle the exception

try:

    file = open(input("enter the file name : "),"r")

    result = file.read()

    print(result)

except FileNotFoundError:

    print("please enter the existing filename!!!!")