from random import randint

#
lower_num, upper_num = 1,10
random_number: int = randint(lower_num, upper_num)
print(f'Guess the number in the range from {lower_num} to {upper_num}.')

#Run an infinite looop for the game
while True:
    #Get the user guess
    try:
        user_guess = int(input('Guess: '))
    except ValueError as error:
        print('Please enter a valid number.')
        continue

    #check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print(f'You guessed it!')
        break