# Display the wages according to gender and age 

g = input('enter your gender:M or F: ')
a = int(input('enter your age: '))
d = int(input('enter no. of days worked: '))

if (a >=18 and a<30) and g.upper() == 'M':
    wage = 700*d
elif (a >=18 and a<30) and g.upper() == 'F':
    wage = 750*d
elif (a >=30 and a<=40) and g.upper() == 'M':
    wage = 800*d
elif (a >=18 and a<30) and g.upper() == 'F':
    wage = 850*d
    
print(wage)
