# create a class details

# method1(name,place,course)

# method2 >> display name and course

class Details:

    def method1(self,name,place,course):
        self.name   = name
        self.place  = place
        self.course = course

        print("welcome")

    def method2(self):

        print(self.name,self.course)

name  = input("Enter your name: ")

place = input("Enter your place: ")

course = input("Enter your Place: ")

obj1 = Details()

obj1.method1(name,place,course)

obj1.method2()