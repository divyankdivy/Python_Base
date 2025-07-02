t_class = int(input('enter total number of calss: '))
a_class = int(input('enter number of class attended: '))

c_per = (a_class/t_class)*100
print(f'your attendance is {round(c_per)}%')

if c_per >= 75:
    print('eligible for exam')
else:
    print('not eligble for exam')
