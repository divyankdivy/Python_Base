# Find the largest number in a list using a for loop:
my_list = [3, 9, 1, 6, 2, 8]
lar_num = my_list[0]
for num in my_list:
    if num>lar_num:
        lar_num = num
print(lar_num)
