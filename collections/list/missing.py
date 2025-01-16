# find missing number from sequence of number


numbers = [6,8,9,4,7]

# numbers.sort()                                           # solving with sorting

# max = numbers[-1]   #9

# min = numbers[0]    #4

# for i in range(min,max+1):

#     if i not in numbers:

#         print(i)

for i in range(min(numbers),max(numbers)+1):               # solving without sorting

    if i not in numbers:

        print(i)
