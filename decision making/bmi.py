""""

Metric units :BMI = Weight (kg) / [Height (m)]^2


Underweight>>Below 18.5
Healthy weight>>18.5 to 24.9
Overweight>>25.0 to 29.9
Obesity>>30.0 or greater
Severe obesity>>40 or over

"""

weight_kg = float(input("Enter your Weight: "))

height_m = int(input("Enter your Height: "))

bmi = weight_kg / height_m ** 2

if bmi < 18.5:
    
    print("Your are Under weight")

elif bmi >= 18.5 and bmi <= 24.9:

    print("You are Healthy")

elif bmi >= 25 and bmi <= 29.9:

    print("You are Overwight")

elif bmi > 30 and bmi <= 40:

    print("Obesity")

else:

    print("You are in Critical Stage.")