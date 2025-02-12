
"""""

COLLECTION
==========

List       :  Collection ,Python used to assign more than one element to variable     === is hetrogenious, it allows duplicates,
                                                                                          it maintains order, 
Tuple      :  Collection ,Python used to assign more than one element to variable  
                                                                                    === 
set        :  Collection ,Python used to assign more than one element to variable  
                                                                                  
Dictionary :  Collection ,Python used to assign more than one element to variable




"""""
# 1 :: List
# =========

# Collection of Python used to assign more than one variable.

# Lists are used to store multiple items in single variable.

# we can store all types of items(including another list)...

# items []

# items = list()

# print(type(items))   <class 'list'>

# items [1,2,3,4]

# items [1,"Hari",True,12.3,False]             >>>> Hetrogenious

items = [1,2,3,4,5]                        #   >>>>  index position

# print(len(items))

# items.append("hari")         # Add an element to last position of the list (items)

# items.insert(2, True)        # To insert an element to a specific index postion

# items.pop(1)                 # Remove and Return item at index (default last(-1))

#print(items.pop(1))

#print(items)

#print(items.count(2))           # number of occurance

# items.sort()                   # return the order in ascending order

# items.sort(reverse=True)       # return the order in decending order

# items.extend([4,8,9,10,0])                 # extend the existing list

# items.index(0)                  # find the index position of number.  return the first index value

# items.clear()                  # return all element clear

# items.remove(4)                 # remove the first index value which is given by us. 
#                                # if there is multiple value it will remove first index value

