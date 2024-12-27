# wap to check voting eligibility

#name =

#age = 

name = input("enter your name: ")

age  = int(input("enter your age: "))

if age < 18:

    print(f"Hi {name} you are not eligible for voting")

elif age >= 18:

    print(f"Hi {name} you are eligible for voting")