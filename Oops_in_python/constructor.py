class Students:

    def __init__(self,name,place):

        self.name = name

        self.place = place

        print("Entered Successfully")

    def display(self):

        print(self.name)

obj1 = Students(name = "Adarsh",place = "Palakkad")

obj1.display()