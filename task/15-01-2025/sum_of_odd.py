#  wap to find the sum of odd numbers in a given list

num = [1, 2, 3, 4, 5]

odd_sum = 0

for i in num:

    if i % 2 != 0:

        odd_sum += i

print(odd_sum)
