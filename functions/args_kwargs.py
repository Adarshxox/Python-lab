# *args, **kwargs

# *args allow you to pass multiple arguments or keyword arguments to a function

# def addition(*args):      # arguments stored in tuple

#     sum = 0

#     for i in args:

#         sum += i

#     print(sum)

# addition(1,2,3)

# addition(1,2)

# addition(1,2,3,4,5,6)


#  **kwargs

# kwargs allow you to pass multiple keyword_arguments to a function

def details(**kwargs):    # {'name': 'adarsh', 'place': 'palakkad', 'position': 'intern'}    stored in dictionary

    print(kwargs)

details(name="adarsh",place="palakkad",position="intern")