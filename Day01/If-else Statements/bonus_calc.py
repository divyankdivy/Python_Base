# Calculate bonus according to salary and years of employees
sal = int(input('enter salary: '))
year = int(input('enter number of years working: '))

if year > 10:
    bon = (10/100)*sal
elif year >=6 and year <=10:
    bon = (8/100)*sal
elif year<6:
    bon = (5/100)*sal
print(round(bon))
