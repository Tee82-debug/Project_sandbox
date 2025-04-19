import random

emojis = {'r' : '🪨', 's': '✂️', 'p': '📄'}
choices = ['r', 'p', 's']

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors?(r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
            print('Invalid Choice!')
        else:
            print('Invalid Choices!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie')
    elif(
        (user_choice == 'r' and computer_choice =='s') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')
        ):
        print('You win!')
    else:
        print('You lose!')

def play_game():

    while True:
        user_choice = get_user_choice()
    
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        
        Proceed = input('Continue? (y/n): ').lower()
        if Proceed == 'n':
            break
    
play_game()


# Ask the user to make a choice 
# # If choice is not valid
#     # Print an error
# Let the computer make a choice
# Determing the winner 
# # Ask the user if they want to continue
#     If not
# Terminate

