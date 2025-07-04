s1 = int(input('enter side of the triangle: '))
s2 = int(input('enter side of the triangle: '))
s3 = int(input('enter side of the triangle: '))

if s1+s2 >s3 and s2+s3>s1 and s1+s3>s2:
    print('triangle is possible')
else:
    print('not possible')
