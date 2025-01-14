#    STRING OPERATIONS

#    =================


name = "adarsh"   # collection sof characters

print(type(name)) # <class str>      >>>  variable name str object

# ASCII Code

name = "hello"   # collections of characters / elements

#       01234      index positioning

# easily fetch           

# update                    

# remove                 

"objectname.methodname()"




"""""

all elements in a string has assigned with a specific index position
> index always starts from 0

advantage
=========

> easily fetch           
> update                    
> remove  


"""

# course = "fullstack"

#         012345678

# print(course[0])     # f     printing the specific element of the string using index value

# print(course[6])

# print(course[0:4])

# print(course[4:9])

course = "fullstack in web applications"

item = course[4]

item = item.upper()

print(course[0:4] + item + course[5::])

# strobject[start:end]      start.....end-1


company_name = "LuminarTechnolab"

# o/p  LUMINAR

print(company_name[0:7].upper())

# o/p TECHNOLAB

print(company_name[7::].upper())

