'Inheritance'

'is a process of inherit all the properties and methods from parent class to child class'


""""

Syntax:
-------

class Parent:                           # Base class

    body of Parent class

class Derivedclass(Parent):             # Derived class

    body of Derived class


"""

# class A(object)                        >>> The base class of the class hierarchy.
    
# Single Inheritance
#-------------------


# class Parent:                                            # Parent class

#     def greeting(self):

#         print("Hello")

# class Child(Parent):                                     # Child class which inherits Parent Class

#     def hello(self):
        
#         print("hey")

#     def greeting(self):                                  # Here the greating is inheriting from Parent class

#         print("Welcome to World")

#         return super().greeting()                        

# obj1 = Child()

# obj1.hello()

# obj1.greeting()


# Types of Inheritance
#---------------------

"""""

1. Single Inheritance

2. Multilevel Inheritance

3. Multiple Inheritance

4. Hierarcal Inheritance

5. Hybrid Inheritance

"""

# Multilevel Inheritance
#-----------------------

# class A:

#     def method1(self):

#         print("hello")

# class B(A):

#     def method2(self):

#         print("I am child")

# class C(B):

#     def method3(self):

#         print("I am the Grand Child")

# child = C()

# child.method3()



# Multiple Inheritance
#---------------------

# a derived class will be inherited from more than one class


class A:

    def meth1(self):

        print("I am A")

class B:

    def meth2(self):

        print("I am B")

class C(A,B):

    def  meth1(self):

        print("I am from A")

        return super().meth1()
    
    def meth2(self):

        print("I am from B")

        return super().meth2()

    def meth3(self):

        print("I am inherited from A & B")

obj1 = C()

obj1.meth1()

obj1.meth2()

obj1.meth3()