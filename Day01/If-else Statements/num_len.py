# Write a program to check whether a number is 3 digit or not

n = int(input("Enter a number"))

l = len(n)
if l == 3:
    print('yes')
else:
    print('no')


# Solution 2

n = int(input('enter number: '))

if n > 99 and n<1000:
    print('Its 3 digit')
else:
    print('No')
