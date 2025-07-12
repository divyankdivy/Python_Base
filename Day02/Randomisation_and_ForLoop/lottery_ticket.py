import random

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

print("Creating 100 random lottery tickets")
lottery_list = []
for i in range(100):
    lottery_list.append(random.randint(1000000000,9999999999))
winners = random.sample(lottery_list,2)
print('2 lucky lottery tickets are',winners)
