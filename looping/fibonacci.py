# wap to print fibanacci series
# 0 1 1 2 3 5 8 13 ............


i = 2

n = int(input("Enter the number of terms: "))


a = 0
b = 1

print("Fibonacci series:")
print(a)
print(b)

while(i<n):             #   2 < 5       

    c = a + b           #   c = 2

    print(c)  

    a, b = b, c         #   a = 1,  b = 1   a = 1, b = 1

    i += 1

# 0 , 1

