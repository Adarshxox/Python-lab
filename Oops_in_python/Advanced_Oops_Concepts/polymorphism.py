# POLYMORPHISM
#-------------

# the literal meaning of polymorphism is the condition of occurrence in different forms.

# it reffers to the use of a single type entity (method, operator or object) to represent different types in different scenerios.

class A:

    def method1(self):

        print("hello")

class B(A):

    def method1(self):

        print("hello world")            # >>>> method overriding 

        return super().method1()
    
obj1 = B()

obj1.method1()
