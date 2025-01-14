"""""

Ask the user to enter a another number. Add these two numbers together and then ask if they want to add another number. If they enter "y", 
ask them to enter another number and keep adding number until they do not answer "y". Once the loop has stopped, display the total.

"""

number1 = float(input("Please enter a number: "))

number2 = float(input("Please enter another number: "))

total = number1 + number2
print("The total is:", total)

while True:

    add_more = input("Do you want to add another number? (y/n): ").lower()
    
    if add_more == "y":

        number = float(input("Please enter another number: "))
        
        total += number
        
        print("The total is:", total)
    else:

        break

print("The final total is:", total)
