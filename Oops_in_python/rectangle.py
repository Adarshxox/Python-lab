# create a class rectangle

# method 1 : length and breadth

# method 2 : perimeter

# method 3 : area

class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

        print("Length and Breadth added successfully")

    def perimeter(self):

        print(f"Perimeter of rectangele is {2*(self.length+self.breadth)}")

    def area(self):

        print(f"Area of Rectangle is {self.length*self.breadth}")

obj1 = Rectangle(length= 10, breadth= 6)

obj1.area()

obj1.perimeter()