# wap to print a list of numbers n to m where n and m entered by user

m = int(input("Enter the starting number (m): "))

n = int(input("Enter the ending number (n): "))

# number = []

# for i in range(m, n + 1):

#     number.append(i)

# print("List of numbers from", m, "to", n, ":", number)

print(list(range(m,n+1)))


