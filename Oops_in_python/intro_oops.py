# class             blueprint for creating objects
#                   it is adesign pattern for objects
#                   collection of objects

# object            is an instance of class.
#                   objects are building blocks of aprogram in OOP, they can be created using classes
#                   Everything in python is object, almost everything has attributes and methods

# list              #  ctrl + click to go builtin segment of python


name = "john"

print(name)


class Addition:

    def sum(a,b):

        return a+b
    
obj = Addition()

obj.sum(3,8)

"""

class Classname :                  >>> Class name in Capital Letter.  Creating a user defined class

    def method1(para1,para2):      >>> creating methods(functions in side class) in the class
    
        statement

        return statement

obj = Classname()                  >>>  creating a object in the class

obj.method1(para1=1)(para2=2)      >>>  only a class object can call its method


"""