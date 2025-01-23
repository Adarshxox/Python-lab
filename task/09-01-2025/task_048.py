"""""

Ask for the name of somebody the user wants to invite to a party. After this display the message "[name] has now been invited" and add 1 to
the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party
and then display how many people they have coimg to the party.

"""
name = input("Enter the name of someone you want to invite to the party: ")

print(f"{name} has now been invited.")

choice = "yes"

count = 1

while (choice== "yes"):

    choice = input("Do you want to invite someone else? (yes/no): ")

    if choice == "yes":

        name = input("enter another name: ")

        print(f"{name} has been invited")

        count += 1

    elif choice == "no":

        print("Thank you")
        

print(f"the toatal number of people are {count}")

