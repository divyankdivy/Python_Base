# Write the program to display all the number that are divisible by 11 and not by 2 between 100 to 500.

l1 = []

for i in range(100,501):
    if i%11 == 0 and i %2!=0:
        l1.append(i)
print(l1)
