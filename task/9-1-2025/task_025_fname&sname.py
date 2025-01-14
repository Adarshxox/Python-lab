"""""

Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter ther surname and join
them together(without a space) and display the name in upper case. If the length of the first name is five characters, display their first 
name in lower case.


"""

f_name = input("Please enter your first name: ")

if len(f_name) < 5:

    surname = input("Please enter your surname: ")

    full_name = f_name + surname

    print(full_name.upper())  

else:

    print(f_name.lower())  

    
