square = lambda num : num**2   # anonymous function

print(square(3))

print(square(56))

"lambda args : expression"

# to find square root of a number given

sq_root = lambda num : num**0.5

print(sq_root(8))

print(sq_root(16))

print(sq_root(10))

# add 2 numbers

add = lambda a,b: a+b

print(add(3,5))

# write a function to check odd or even

result = lambda a : "even" if a % 2 == 0 else "odd"

print(result(5))