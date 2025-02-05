from functools import reduce

# write a lambda function that takes a list of numbers and return new list with each one tripled

# [1,2,3]  >>  [1,8,27]

# result = lambda a : [i**3 for i in a]

# print(result(a = [1,2,3]))


# write a lambda function that a list of numbers and return new list with even numbers

# result1 = lambda b : [i for i in b if i % 2 == 0]

# print(result1(b=[1,2,3,4,5,6,7,8,9]))


# write a lambda function which takes a string and returns the string in reverse

# reverse = lambda a : a[::-1]

# print(reverse("hello"))


# pritn result in list

# num = [1,3,5,7,9,2,4,6,8]

# def square(a):

#     return a ** 2

# numbers = [square(i) for i in num]

# print(numbers)

# print(list(map(lambda a : a**2,num)))

# map(args1{function},args2{list})

# map() function is used to apply a given function to every time of an iterable, such as a list or tuple


# convert a list of string to uppercase using map() and lambda

# words = ["hello","world"]

# print(list(map(lambda a : a.upper(),words)))



# numbers = [1,2,3,4]

# print(list(map(lambda item : item**2,numbers)))



" filter, reduce "

# num = [1,2,3,4,5,3,6,7,8,10]   # extract even numbers from the list

# print(list(filter(lambda a : a%2==0,num)))

# filters the given sequence with the help of a function that tests each element in the sequence to be true or not

# num = [1,2,3,4]  #sum of numbers in list 10

# print(reduce(lambda a,b:a+b,num))


num = [4,1,5,6,7,8,10,3,7]

# apply a function to double each elements
# then extract the numbers greater than 10 and take the product of numbers

double = list(map(lambda a : a*2, num))

print(double)

greater = list(filter(lambda a : a > 10, double))

print(greater)

print(reduce(lambda a,b : a*b , greater))