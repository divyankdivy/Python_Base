# Write a program to display all prime numbers within a range

start_num = int(input('enter starting number: '))
end_num = int(input('enter ending number: '))

for num in range(start_num, end_num+1):
    
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num,end = ', ')
