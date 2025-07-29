# Count the number of vowels in a string using a for loop:

st = 'Hello World'

vowl = 'AEIOUaeiou'

count = 0

for char in st:
    if char in vowl:
        count += 1
print('total number of vowel in string is:',count)
