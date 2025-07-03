n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))

o = input('enter math operator ')

if o =='+':
    cal = n1+n2
elif o == '-':
    cal = n1-n2
elif o == '*':
    cal = n1*n2
elif o == '/':
    cal = n1/n2
print(round(cal))
