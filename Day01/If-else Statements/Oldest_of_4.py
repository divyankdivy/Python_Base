a1 = int(input('enter age 1: '))
a2 = int(input('enter age 2: '))
a3 = int(input('enter age 3: '))
a4 = int(input('enter age 4: '))

if a1>a2 and a1>a3 and a1>a4:
    print(a1,'is oldest')
elif a2>a1 and a2>a3 and a2>a4:
    print(a2,'is oldest')
elif a3>a2 and a3>a1 and a3>a4:
    print(a3,'is oldest')
elif a4>a2 and a4>a3 and a4>a1:
    print(a4,'is oldest')
