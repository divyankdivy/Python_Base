n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))
n3 = int(input('enter number 3: '))

if n1>n2 and n1>n3:
    print(f'{n1} is the greatest.')
elif n2>n1 and n2>n3:
    print(f'{n2} is the greatest.')
elif n3> n2 and n3>n1:
    print(f'{n3} is the greatest.')
