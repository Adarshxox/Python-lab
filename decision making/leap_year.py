
# wap to find leap year or not

year = int(input("Enter the Year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 100 == 0:

    print(f"{year} is Leap Year ")

#elif year % 400 == 0 and year % 100 == 0:

    #print(f"{year} is Leap Year and its Century Year")

else:

    print(f"{year} is not a Leap Year")

