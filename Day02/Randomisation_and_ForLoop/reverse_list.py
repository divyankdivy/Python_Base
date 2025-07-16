#  Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
rev_list = []

for i in list1[::-1]:
    rev_list.append(i)
print(rev_list)
