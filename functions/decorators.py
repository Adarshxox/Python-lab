# DECORATORS
#-----------

# functions that can modify the behavior of other functions, classes, or methods without modifing its structure


def swap_numbers(fctn):

    def wrapper(x,y):

        if y == 0:

            x,y = y,x

        return fctn(x,y)
    
    return wrapper


@swap_numbers
def division(a,b):

    print(a/b)

division(4,6)

division(4,0)