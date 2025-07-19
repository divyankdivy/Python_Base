# Find the factorial of a given number

num = int(input('enter number: '))
facto = 1

if num == 0 or num == 1:
    facto = 1
elif num>1:
    for i in range(2, num+1):
        facto *= i
print(facto)
