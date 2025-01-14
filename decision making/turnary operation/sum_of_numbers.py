# sum of three numbers is even or odd

num1 = int(input("enter the number: "))

num2 = int(input("enter the number: "))

num3 = int(input("enter the number: "))


print("even" if (num1 + num2 + num3) % 2 == 0 else "odd")