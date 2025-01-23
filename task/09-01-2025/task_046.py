"""""

Ask the user to enter a number. Keep asking until they enter value over 5 and then display the message "last number you entered was a 
[number] and stop the program.

"""

number = float(input("Please enter a number: "))


while True:
    
    if number > 5:
        
        print("The last number you entered was a", number)
        
        break  
