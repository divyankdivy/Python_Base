# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# Unit                            Price
# First 100 units               no charge
# Next 100 units               Rs 5 per unit
# After 200 units              Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

unit = int(input('enter the units: '))
bill = 0

if unit<0:
    print('enter correct unit')
elif unit <= 100:
    bill = 0
    print(f"your bill is {bill}")
elif 100 < unit <= 200:
  bill = (unit - 100) * 5
  print(f"your bill is {bill}")
elif unit > 200:
  bill = 500 + (unit - 200) * 10
  print(f"your bill is {bill}")
