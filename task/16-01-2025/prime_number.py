# wap to find the prime numbers from the list

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = []

for i in numbers:

    if i > 1:

        prime = True

        for j in range(2, i):

            if i % j == 0:

                prime = False

                break

        if prime:

            prime_numbers.append(i)

print("Prime numbers:", prime_numbers)