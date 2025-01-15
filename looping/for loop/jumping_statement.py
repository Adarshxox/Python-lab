# jumbing statements
#===================

# while loop >> condion based

# for loop >> quantity based

# break, continue, pass


"# wap to print 1 to 10"

for i in range(1,11):   # divisible by 5

    print(i)            # 1 2 3 4 5

    if i % 5 == 0:      # 5 % 5 == 0  True
      
       break            # is used to exit the a loop when a certain condition is met

for i in range(1,11):

    if i % 3 == 0:

         continue       # used to skip an iteration when a condition is met
    else:
         print(i)       # 1 2 4 5 7 8 10

