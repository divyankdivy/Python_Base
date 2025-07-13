import random

 You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

name = input('enter names:\n').split(', ')
name_len = len(name)
name_choice = random.randint(0,name_len-1)
print(name[name_choice],'is going to pay the bill.')
