"""
Create a dictionary of five countries and their capitals.User need to input a  countryname if the country name is in the 
dictionary retrun its capital and if it is not in dicitonary retrun "Not found" 

Afghanistan: The capital of Afghanistan is Kabul.
Albania: The capital of Albania is Tirana.
Algeria: The capital of Algeria is Algiers.
Andorra: The capital of Andorra is Andorra la Vella.
Angola: The capital of Angola is Luanda.


>>>   {"Afghanistan":"Kabul","Albania":"Tirana","Algeria":"Algiers","Andorra":"Andorra la Vella","India":"Delhi"}


"""

country = {"Afghanistan":"Kabul","Albania":"Tirana","Algeria":"Algiers","Andorra":"Andorra la Vella","India":"Delhi"}

country_name = input("Enter the country name: ")

country_name.capitalize()

if country_name in country:

    print(country[country_name])

else:

    print("Not Found")