fruit_prices = {"apple": 0.50, "banana":0.75, "orange":0.80}

for i in fruit_prices.copy():

    if i == "orange":

        fruit_prices.pop(i)

        fruit_prices["grape"] = 0.90

print(fruit_prices)
