
numbers = [1,2,3,4,5,6,7]               # o/p   ==  [5,6,7,1,2,3,4]

print(numbers)

for i in range(3):

    last = numbers.pop()                    # last == 7

    numbers.insert(0,last)

print(numbers)
