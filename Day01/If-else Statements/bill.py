km = int(input('enter the kilometers: '))
bill = 0

if km<=10:
    bill = km*11
elif km > 10 and km<=100:
    bill = 110 +(km-10)*10
elif km>100:
    bill = 1010 +(km-100)*9
print(bill)
