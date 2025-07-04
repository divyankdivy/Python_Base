# Display second largest

n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))
n3 = int(input('enter number 3: '))

if (n1>n2 and n2>n3) or (n2>n1 and n3>n2):
    print(f'{n2} is the second.')
elif (n2>n1 and n1>n3) or (n3>n1 and n1>n2):
    print(f'{n1} is the second.')
elif (n1> n3 and n3>n2) or (n2>n3 and n3>n1):
    print(f'{n3} is the second.')
