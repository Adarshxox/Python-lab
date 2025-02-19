# class student

# method1 (name,age,mark)

# method2 (update mark)

# method3 (delete student record)

class Student:

    def __init__(self):
        
        self.student = {}                                         # create an empy dictionary

    def add_data(self,name,age,mark):

        self.name = name

        self.age = age

        self.mark = mark

        self.student[name] = {'age':age,'mark':mark}             # inside dictionary creating another one

        print("Data uploaded successfully")

        print(self.student)

    def update_mark(self,name,up_mark):

        self.student[name]["mark"] = up_mark

        print("Mark update complete")

        print(f"updated mark : {up_mark}")

        print(self.student)

    def delete_student_record(self,name):

        self.student

        print("Record Removed Successfully")

obj1 = Student()

obj1.add_data(name="adarsh",age=25,mark=750)

obj1.update_mark(name="adarsh",up_mark=800)


