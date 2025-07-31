# Write the sum of odd and even number that fall between two given numbers.

n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))

sum_odd = 0
sum_even = 0

for i in range(n1,n2):
    if i%2==0:
        sum_even +=i
    else:
        sum_odd += i
print(sum_even)
print(sum_odd)
