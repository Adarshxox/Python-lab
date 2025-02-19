def merge_sorted(list1, list2):

    merged = []

    i, j = 0, 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:

            merged.append(list1[i])

            i += 1

        else:

            merged.append(list2[j])

            j += 1

    merged.extend(list1[i:])

    merged.extend(list2[j:])

    return merged

print(merge_sorted([1,3,5], [2,4,6]))

print(merge_sorted([10,20],[5,15,25]))

