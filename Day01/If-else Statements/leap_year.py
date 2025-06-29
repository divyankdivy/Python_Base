# Write a program to check whether an years is leap year or not.

print("Check whether Year is Leap or not")

year = int(input('enter year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not Leap')
    else:
        print('Leap Year')
else:
    print('Not Leap')
