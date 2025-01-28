# find smallest in three numbers

def smallest(a, b, c):

    if a < b and a < c:

        print(f"{a} is the smallest")

    elif b < c and b < a:

        print (f"{b} is the smallest")

    else:

        print(f"{c} is the smallest")

smallest(10,25,111)