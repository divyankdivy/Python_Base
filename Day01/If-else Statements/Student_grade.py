# Write a program to accept percentage from the user and display the grade according to the criteria:

marks = int(input('enter your marks: '))

if marks<0:
    print('enter correct marks')
elif marks>100:
    print('enter correct marks')
elif marks>90 and marks <= 100:
    print('A')
elif marks >80 and marks<=90:
    print('B')
elif marks >=60 and marks<=80:
    print('C')
elif marks <60:
    print("D")
