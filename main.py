# importing colors module
from colors import *
# Importing random module
from random import randint


# Welcome screen
print(YELLOW, '***** welcome to Lover-Game *****')
user_input = int(input(WHITE + '1. Start Game \n'
      '2. About Lover-Game\n'
      '3. Exit Application\n\n'
      'Choose an option above: '))

# Determine user input
if user_input == 1:
      user_input = int(input(WHITE + 'Choose Game Level\n'
            '1. Lazy (1 - 100)\n'
            '2. Intermediate (1 - 500)\n'
            '3. Hard (1 - 1000)\n\n'
            'Provide Level:  '))

      # Determine the guess range
      guess_range = 0
      if user_input == 1:
            guess_range = 100
      elif user_input == 2:
            guess_range = 500
      elif user_input == 3:
            guess_range = 1000

#       generate random number base on the guess range
      generated_namber = randint(1, guess_range)
#       user guessing attempt
      user_chance =3
      for chance in range(3):
            user_guess = int(input(WHITE + 'Provide your guess number: '))
#            Determin/validate user guess
            if user_guess == generated_namber:
                  print(GREEN, f'Congratulations!! You Guessed {generated_namber} Right')
                  break
            elif user_guess > generated_namber:
                  print(RED_BOLD_BRIGHT, f'{user_guess}Too High, Try Again!!!')
                  user_chance -= 1
            elif user_guess < generated_namber:
                  print(BLUE_BOLD_BRIGHT, f'{user_guess} Too Low, Try Again!!!')
                  user_chance -= 1
      if user_chance < 1:
            print(RED_BOLD_BRIGHT, f'You faid, Try Again!!!\n'
                  f'The Correct Guessed Number is {generated_namber}')





elif user_input == 2:
      print(YELLOW, 'Lover Game: Guessing of numbers')
elif user_input == 3:
      print(WHITE, 'Hope to see you again, gamer!')
      exit(1)
else:
      print(RED, 'Invalid option, Try again!!!')