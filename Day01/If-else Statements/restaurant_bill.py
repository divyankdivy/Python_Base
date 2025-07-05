# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

size = input('enter pizza size: S,M or L ')
price = 0

if size.upper() == 'S':
    price = 15
elif size.upper() == 'M':
    price = 20
elif size.upper() == 'L':
    price = 25
    
print(f'these are the price without any add on: ${price}')

pep = input('do you want to add pepperoni? Y or N: ')

if pep.upper() == 'Y' and size.upper() == 'S':
    price += 2
elif (pep.upper() == 'Y' and size.upper() == 'M') or (pep.upper() == 'Y' and size.upper() == 'L'):
    price += 3
    
cheese = input('do you want to add cheese? Y or N: ')

if cheese.upper() == 'Y':
    price+=1

print(f'Your final bill is: ${price}')
