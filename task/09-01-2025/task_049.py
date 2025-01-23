"""""

Create a variable called compnum and st the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum 
value, tell them if their guess is too low or too hish and ask them to have another guess. iF they enter the same value as compnum display
the value

"""

compnum = 50

while True:
    
    guess = int(input("Guess a number: "))

    if guess == compnum:

        print("Congratulations! You guessed the correct number:", compnum)
        break
    elif guess < compnum:

        print("Your guess is too low. Try again.")
    else:

        print("Your guess is too high. Try again.")
