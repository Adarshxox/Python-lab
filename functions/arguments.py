def details(name,place,position):                     # keyword arguments

    print(f"Hi {name} you are from {place} and your position is {position}")

details(position="Intern", place="Palakkad",name="Adarsh")

" send arguments with key = value syntax. this way the order of the arguments does not matter "

def details1(name,place,position="Intern"):             # default arguments

    print(f"Hi {name} you are from {place} and your position is {position}")

details1(place="Bangalore",name="Adarsh")

" Default arguments in Python are the function arguments that will be used if no arguments are passed to the function call. "