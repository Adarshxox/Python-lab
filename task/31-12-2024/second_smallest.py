a = int(input("enter the first number:"))

b = int(input("enter the second number:"))

c = int(input("enter the third number:"))


if (a < b and a > c) or (a < c and a > b) :

    print(f"{a} is second smallest number")
    
elif (b < a and b > c) or (b < c and b > a ) : 

    print(f"{b} is second smallest number")

elif (c < a and c > b) or (c < b and c > a ) : 

    print(f"{c} is second smallest number")