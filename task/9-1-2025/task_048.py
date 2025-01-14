"""""

Ask for the name of somebody the user wants to invite to a party. After this display the message "[name] has now been invited" and add 1 to
the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party
and then display how many people they have coimg to the party.

"""

invi_count = 0

while True:
    
    name = input("Enter the name of someone you want to invite to the party: ")

    print(name + " has now been invited.")

    invi_count += 1

    invi_more = input("Do you want to invite someone else? (y/n): ").lower()

    if invi_more != "y":
        
        break

print("You have " + str(invi_count) + " people coming to the party.")
