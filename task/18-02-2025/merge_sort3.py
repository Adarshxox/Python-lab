merged_list = list1 + list2

n = len(merged_list)

for i in range(n):

    for j in range(0, n - i - 1):

        if merged_list[j] > merged_list[j + 1]: 

            merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

print(merged_list)
