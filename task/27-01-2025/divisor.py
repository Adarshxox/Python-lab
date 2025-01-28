# find divsors of number

def divisors(num):

    for i in range(1,num):

        if num % i == 0:

            print(i)

divisors(6)

