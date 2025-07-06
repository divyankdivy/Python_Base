# Roller Coaster Ride Ticket Prices Calculations

print("Welcome to the Roller Coaster")

height = int(input('enter your height in cm: '))
price = 0

if height > 120:
    print('You can ride.')
    age = int(input('enter your age: '))
    if age<12:
        price +=5
    elif age >=12 and age <= 18:
        price+=7
    elif age >= 45 and age <=55:
        price += 0
        print('Enjoy have a free ride on us')
    elif age>18:
        price+= 12 
        
    photos = input('do you want photos? Y or N: ')
    if photos.upper() == 'Y':
        price+= 3
    print(f'Your Total bill is : ${price}')
else:
    print('You are not eligible to ride.')
