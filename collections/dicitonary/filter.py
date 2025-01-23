mobiles={"Apple":{"model":"iphone15","price":120000,"color":"Black"},
         "Samsung":{"model":"S23 Ultra","price":180000,"color":"white"},
         "Sony":{"model":"xperia ultra","price":130000,"color":"red"},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":"Black"}
         }

print("The mobiles using Black colors")

print("==============================")

for i in mobiles:

    if mobiles[i]["color"] == "Black":

        print(i)


# price above 50k

print("The mobiles price above 50k")

print("===========================")

for i in mobiles:

    if mobiles[i]["price"] > 50000:

        print(i)

# iphone / xperia

# colors other than black

print("The mobiles using colors other than black")

print("=========================================")

for i in mobiles:

    if mobiles[i]["color"] != "Black":

        print(i)

# Black in color and price less than 150k

print("Black in color and price less than 150k")

print("=======================================")

for i in mobiles:

    if mobiles[i]["color"] == "Black" and mobiles[i]["price"] > 150000:

        print(i)


# print the modelname ending with "ultraa"