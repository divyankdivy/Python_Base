# find prime number between two given numbers
n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))

for num in range(n1,n2):
    if num>1:
        for i in range(2,num):
            if num%i ==0:
                break
        else:
            print(num)
