# grade selector

# marks

# greater than 90 >> A grade

# greater than 80 and less than or equal to 90 >> B grade

# greater than 70 and less than or equal to 80 >> C grade

# greater than 60 and less than or equal to 70 >> D grade

# greater than 50 and less than or equal to 60 >> E grade

# less than 50 >> failed please try again


mark = int(input("enter your mark: "))

if mark > 90 and mark <= 100:

    print("You hava A grade")

elif mark > 80 and mark <= 90:

    print("You have B grade")

elif mark > 70 and mark <= 80:

    print("You have C grade")

elif mark > 60 and mark <= 70:

    print("You have D grade")

elif mark >= 50 and mark <= 60:

    print("You have E grade")

else:

    print("You Failed!! Better luck next time")


