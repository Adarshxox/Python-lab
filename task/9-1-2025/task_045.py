"""""

set the total to 0 to start with. While the total is 50 or less, ask the user to input a number.
add that number to the total and print the message "the total is...[total]". stop the loop when the total is over 50. 

"""

total = 0

while total <= 50:
   
    number = float(input("Please enter a number: "))
    
    total = total + number
    
    print("The total is... " + str(total))
