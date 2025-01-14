"""""

Ask the user if it is raining and convert their answer to lower case so it doesnt matter what case they type it in. If they answer "yes"
ask if it is windy. If they answer "yes" to this second question, display the answer "it is too windy for an umbrella", otherwise display 
the message "take a umbrella". if they did not answer yes to the first question, display the answer "enjoy the day".

"""


is_raining = input("Is it raining? (yes/no): ").lower()

if is_raining == "yes":

    is_windy = input("Is it windy? (yes/no): ").lower()
    

    if is_windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy the day.")
