""""


Ask the user to enter the number. If the number is under 10, >> "Too Low",
number between 10 & 20 (inclusive), >> "Correct", otherwise display "Too High".


"""


number = int(input("Enter the number: "))

if number < 10:

    print("Too Low")

elif number >= 10 and number <= 20:

    print("Correct")

else:

    print("Too High")

