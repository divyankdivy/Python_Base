# Calculate the discount

price = int(input('enter the price of item'))
d = 0

if price > 10000:
    d = (20/100)*price
elif price>7000 and price <= 10000:
    d = (15/100)*price
elif price<=7000:
    d = (10/100)*price

amount_to_pay = price - d
print(amount_to_pay)
