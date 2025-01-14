# temp less than 20                    >> COLD

# temp between 20 to 30 (inclusive)    >> WARM

# greater than 30                      >> HOT


temp = int(input("enter the temperature: "))

print("COLD" if temp < 20 else "WARM" if temp >= 20 and temp <= 30 else "HOT")