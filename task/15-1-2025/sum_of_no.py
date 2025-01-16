# wap to ask user to enter the number to the list until the sum of number in list reach 50

numbers = []

sum = 0  

num = int(input("Enter a number: ")) 

while sum < 50:

    if sum + num > 50:

        print("The number is too large. Try again.")
    
    else :

        numbers.append(num)

        sum += num  

    if sum  < 50:

        num = int(input("Enter a number: "))

print("The numbers are:", numbers)

print("The sum of the numbers is:", sum)



