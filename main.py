# importing colors module
from colors import *
# Importing random module
from random import randint

def game_level():
    user_input = int(input(WHITE + 'Choose Game Level\n'
                                   '1. Lazy (1 - 100)\n'
                                   '2. Intermediate (1 - 500)\n'
                                   '3. Hard (1 - 1000)\n\n'
                                   'Provide Level:  '))
    return user_input

def user_guess_range(user_input):
    guess_range = 0
    if user_input == 1:
        guess_range = 100
    elif user_input == 2:
        guess_range = 500
    elif user_input == 3:
        guess_range = 1000

    return guess_range


def user_guess(guess_range):
    #       generate random number base on the guess range
    generated_number = randint(1, guess_range)
    #       user guessing attempt
    user_chance = 3
    for chance in range(3):
        user_guess = int(input(WHITE + 'Provide your guess number: '))


        #            Determin/validate user guess
        if user_guess == generated_number:
            print(GREEN, f'Congratulations!! You Guessed {generated_number} Right')
            break
        elif user_guess > generated_number:
            print(RED_BOLD_BRIGHT, f'{user_guess}Too High, Try Again!!!')
            user_chance -= 1
        elif user_guess < generated_number:
            print(BLUE_BOLD_BRIGHT, f'{user_guess} Too Low, Try Again!!!')
            user_chance -= 1
    if user_chance < 1:
        print(RED_BOLD_BRIGHT, f'You failed, Try Again!!!\n'
                               f'The Correct Guessed Number is {generated_number}')


# Welcome screen
def welcome_screen():
    print(YELLOW, '***** welcome to Lover-Game *****')
    user_input = int(input(WHITE + '1. Start Game \n'
                                    '2. About Lover-Game\n'
                                    '3. Exit Application\n\n'
                                    'Choose an option above: '))

# Determine user input
    if user_input == 1:
        user_input = game_level()


        # Determine the guess range
        guess_range = user_guess_range(user_input)


        user_guess(guess_range)


    elif user_input == 2:
        print(YELLOW, 'Lover Game: Guessing of numbers')
        welcome_screen()
    elif user_input == 3:
        print(WHITE, 'Hope to see you again, gamer!')
        exit(1)
    else:
        print(RED, 'Invalid option, Try again!!!')
        welcome_screen()

welcome_screen()