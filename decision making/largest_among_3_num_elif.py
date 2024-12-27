

# largest among 3 numbers

# a , b , c


a = int(input("enter the number:")) # 4

b = int(input("enter the number:")) # 8

c = int(input("enter the number:")) # 10


if a > b and a > c:  # true and false     if false

    print(f"{a} is largest")
    
elif b > a and b > c: 

    print(f"{b} is largest")

else:

    print(f"{c} is largest")