# Check if a number is perfect
def perfect_num(a):

    sum = 0
    
    i = 1

    while i < a:

        if a % i == 0:

            print(i)

            sum += i

        i += 1

    if sum == a:

        print(f"{a} is a perfect number")

    else:

        print(f"{a} is not a perfect number")

perfect_num(28)