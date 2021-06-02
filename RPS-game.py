# Rock-Paper-Scissors Game

from random import randint

# movees for the player
moves = ['rock', 'paper', 'scissors']

while True:
  computer = moves[randint(0, 2)]
  player = input('rock, paper or scissors? (or end) ').lower()
  if player == 'end':
    print('the game as ended.')
    break
  elif player == computer:
    print('Tie!!!')
  elif player == 'rock':
    if computer == 'paper':
      print('You lose!', computer, 'beats', player)
    else:
      print('You win!', player, 'beats', computer)
  elif player == 'paper':
    if computer == 'scissors':
      print('You lose!', computer, 'beats', player)
    else:
      print('You win!', player, 'beats', computer)
  elif player == 'scissors':
    if computer == 'rock':
      print('You lose!', computer, 'beats', player)
    else:
      print('You win!', player, 'beats', computer)
  else:
    print('Check your spelling...')
