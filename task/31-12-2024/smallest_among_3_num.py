
# largest among 3 numbers

# a , b , c


a = int(input("enter the first number:")) # 4

b = int(input("enter the second number:")) # 8

c = int(input("enter the third number:")) # 10


if a < b and a < c:  # true and false     if false

    print(f"{a} is smallest")
    
elif b < a and b < c: 

    print(f"{b} is smallest")

else:

    print(f"{c} is smallest")