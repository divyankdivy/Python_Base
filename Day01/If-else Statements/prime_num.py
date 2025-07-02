# Check a number is prime or not
n = int(input('enter number: '))
k = 0
for i in range(2,n):
    if n%i ==0:
        k+=1
if k == 0:
    print('prime')
else:
    print('not prime')
