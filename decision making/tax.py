
# cost of the bike above 100000 add 15% tax to the price

# if cost of the bike is greater than 50k and less than 1lakh (both inclusive) add tax 10%

# if cost < 50k tax is 7%

price = int(input("enter the amount: "))

if price > 100000:

    tax = price * 15/100

    print(f"Your total cost is {price + tax}")

elif price >= 50000 and price <= 100000:

    tax = price * 10/100

    print(f"Your total cost is {price + tax}")

else:

    tax = price * 7/100

    print(f"Your total cost is {price + tax}")

