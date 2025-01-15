# wap to print a list of numbers n to m where n and m entered by user

n = int(input("Enter the starting number (n): "))

m = int(input("Enter the ending number (m): "))

number = []

for i in range(n, m + 1):

    number.append(i)

print("List of numbers from", n, "to", m, ":", number)
