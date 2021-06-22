# Haven't even started
import random
import math

def printGameboard(gameboard):
	print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3] + ' ')
	print('---+---+---')
	print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6] + ' ')
	print('---+---+---')
	print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9] + ' ')
	print()


def isGameOver(gameboard):
	# Loop through rows, columns, and diagonals to check if there 
    # are 3 identical pieces on a line. If so, game is over.
    # 
    # Game is also over if all pieces are filled.

	if (gameboard[1] == gameboard[2] == gameboard[3] != ' ' or gameboard[4] == gameboard[5] == gameboard[6] != ' ' or gameboard[7] == gameboard[8] == gameboard[9] != ' ' or
	gameboard[1] == gameboard[4] == gameboard[7] != ' ' or gameboard[2] == gameboard[5] == gameboard[8] != ' ' or gameboard[3] == gameboard[6] == gameboard[9] != ' ' or
    gameboard[1] == gameboard[5] == gameboard[9] != ' ' or gameboard[3] == gameboard[5] == gameboard[7] != ' ' or all(i != ' ' for i in gameboard.values())):
		return True
	return False


def endingText():
	print('\n--------------------')
	print('|    Game Over!    |')
	print('|                  |')
	print('| Thx for Playing! |')
	print('--------------------\n')


def decideWinner(gameboard, turn):
	if turn[1]: # Player's turn
		if any(i == ' ' for i in gameboard.values()):
			print('\nAwww! You lost!')
		else:
			print('\nYou tie!')
		endingText()
	elif turn[0]: # Computer's turn
		if any(i == ' ' for i in gameboard.values()):
			print('\nCongratulations! You won!')
		else:
			print('\nYou tie!')
		endingText()


def endingText():
	print('\n--------------------')
	print('|    Game Over!    |')
	print('|                  |')
	print('| Thx for Playing! |')
	print('--------------------\n')
