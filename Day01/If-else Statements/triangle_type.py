s1 = int(input('enter side of the triangle: '))
s2 = int(input('enter side of the triangle: '))
s3 = int(input('enter side of the triangle: '))

if s1 == s2 and s1 == s3:
    print('equilateral triangle')
elif (s1 != s2) and (s2!= s3) and (s1!= s3):
    print('scalene triangle')
elif (s1==s2 or s1!= s3) or (s1==s3 and s1!= s2) or (s2 == s3 and s2!=s1):
    print('isoscales triangle')
