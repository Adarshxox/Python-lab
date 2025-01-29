# create a function and remove duplicates that removes duplicate elemets from a list and returns the new list

# [1,2,3,2,3,4,5]        >>>   [1,2,3,4,5]

def remove_dulpicate(elements):

    new = []

    for i in elements:

        if i not in new:

            new.append(i)

    print(new)

remove_dulpicate([1,2,3,2,3,4,5])