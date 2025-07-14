# Calculate the sum of all numbers from 1 to a given number

number = int(input('enter a number'))
summ = 0
for num in range(1, number+1):
    summ+=num
print(summ)
