# Display Fibonacci series up to nth terms

n = int(input('enter number: '))

f_num = 0
s_num = 1
print(f_num, end = ', ')
print(s_num, end = ', ')

for i in range(2,n):
    t_num = f_num+s_num
    print(t_num,end = ', ')
    f_num = s_num
    s_num = t_num
