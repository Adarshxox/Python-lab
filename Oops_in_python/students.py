# create class name Student

# method 1 : suppose to get marks of subject1,subject2,subject3

# method 2 : print the average

class Student():

    def marks(self,sub1,sub2,sub3):

        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

        print("Marks added Successfully")

    def average(self):

        print((self.sub1+self.sub2+self.sub3)/3)

obj1 = Student()

obj1.marks(sub1=80,sub2=76,sub3=67)

obj1.average()