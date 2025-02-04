"""""

Given two lists:
lst1 = ["apple", "mango", "orange", "kiwi"]
lst2 = [100, 200]
Write a Python program to create a dictionary where:
1.The keys are elements from lst1 and the values are the corresponding elements from lst2 (for indices where lst2 has values).
2.For the remaining elements in lst1 (if any), assign values starting from 1 incrementally.
Example Output:
Output: {"apple": 100, "mango": 200, "orange": 1, "kiwi": 2}

"""

lst1 = ["apple", "mango", "orange", "kiwi"]

lst2 = [100, 200]

result = {lst1[i] : lst2[i] if i < len(lst2) else i - len(lst2) +1 for i in range(len(lst1)) }

print(result)