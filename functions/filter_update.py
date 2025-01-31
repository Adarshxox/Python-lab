"""
Create a nested dictionary of three employees, each with keys for name, age, and salary. 
Write a function to give each employee a 10% raise and print the updated dictionary.
"""
employees = {"emp1":{"name":"ram","age":25,"salary":15000},
             "emp2":{"name":"hari","age":30,"salary":10000},
             "emp3":{"name":"ak","age":32,"salary":20000}}


# for i in employees:

#     print("salary before update:",employees[i]["salary"])

#     print("updated salary:", employees[i]["salary"] + employees[i]["salary"]*10/100)


# using function method

def salary_hike(emp):

    for i in emp:

        emp[i]["salary"] += emp[i]["salary"]*10/100

    print(emp)

salary_hike(emp=employees)