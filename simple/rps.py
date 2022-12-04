import random
import time

computer_score = 0
player_score = 0
while computer_score < 2 and player_score < 2:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None
    result = None

    while player not in choices:
        player = input('rock, paper, or scissors? : ').lower()
        if player not in choices:
            print('Try again.')

    if player == computer:
        result = 'It\'s a tie!'

    elif player == 'rock':
        if computer == 'paper':
            computer_score += 1
            result = 'You lost this round...'
        elif computer == 'scissors':
            player_score += 1
            result = 'You won this round!'
    elif player == 'paper':
        if computer == 'scissors':
            computer_score += 1
            result = 'You lost this round...'
        elif computer == 'rock':
            player_score += 1
            result = 'You won this round!'
    elif player == 'scissors':
        if computer == 'rock':
            computer_score += 1
            result = 'You lost this round...'
        elif computer == 'paper':
            player_score += 1
            result = 'You won this round!'

    print(f'computer: {computer}')
    print(f'player: {player}')
    print(result)
    print(f'{player_score} - {computer_score}')

    time.sleep(1)

    if player_score == 2:
        print('\n-+= Player wins! =+-')
    if computer_score == 2:
        print('\n-+= Computer wins! =+-')
