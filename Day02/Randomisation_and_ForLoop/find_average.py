# Find the average of numbers in a list using a for loop

my_list = [3, 9, 1, 6, 2, 8, 10, 12]

summ = 0

for num in my_list:
    summ+=num
    avge = summ/len(my_list)
print(round(avge,2))
