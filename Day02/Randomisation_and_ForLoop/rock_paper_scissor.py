#  Rock-Paper-Scissors Game

print("Welcome to Rock Paper Scissors")

print('Choose 1 for Rock\nChoose 2 for Paper\nChoose 3 for Scissor')

user_choice = int(input('select a number between 1 to 3: '))
print('the option chose by user is',end =' ')
if user_choice == 1:
    print('Rock')
elif user_choice == 2:
    print('Paper')
elif user_choice == 3:
    print('Scissor')

comp = random.randint(1,3)
print('the option chose by computer is',end =' ')
if comp == 1:
    print('Rock')
elif comp == 2:
    print('Paper')
elif comp == 3:
    print('Scissor')

if user_choice == comp:
    print('Tie')
elif user_choice == 1 and comp == 2:
    print('You Loose')
elif user_choice == 1 and comp == 3:
    print('You win')
elif user_choice == 2 and comp == 1:
    print('You win')
elif user_choice == 2 and comp == 3:
    print('You Loose')
elif user_choice == 3 and comp == 1:
    print('You loose')
elif user_choice == 3 and comp == 2:
    print('You Win')
