# create a class calculator

# methods  >> addition, subtraction, division, multiplication, modulus

class Calculator:

    def addition(self,x,y):

        print(f"addition of {x} and {y} : {x+y}")

    def subtraction(self,x,y):
        
        print(f"subtract of {x} and {y} : {x-y}")

    def division(self,x,y):

        print(f"division of {x} and {y} : {x/y}")

    def multiplication(self,x,y):

        print(f"multiply  {x} and {y} : {x*y}")

    def modulus(self,x,y):

        print(f"modulus of {x} and {y} : {x%y}")

obj = Calculator()

obj.addition(2,3)

obj.subtraction(6,2)

obj.multiplication(5,7)

obj.division(6,2)

obj.modulus(5,2)
