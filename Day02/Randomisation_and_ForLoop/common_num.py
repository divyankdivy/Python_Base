# Find the common elements in two lists using a for loop:

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)
print(list3)
