import random
import math

playerTurn = False
cpuTurn = False
board = {
	7: ' ', 8: ' ', 9: ' ', 
	4: ' ', 5: ' ', 6: ' ', 
	1: ' ', 2: ' ', 3: ' ', 
}

def printGameboard(gameboard):
	print()
	print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3] + ' ')
	print('---+---+---')
	print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6] + ' ')
	print('---+---+---')
	print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9] + ' ')
	print()

def cpuRandomMove(gameboard):
	print('\nComputer\'s move: ')
	available = []

	for i in range(1, 10):
		if gameboard[i] == ' ':
			available.append(i)
	
	randChoice = random.choice(available)
	gameboard[randChoice] = 'X'
	printGameboard(gameboard)


def playerMove(gameboard):
	print('It\'s your turn now! Which place would you like to move to?')
	moveNum = int(input())

	if gameboard[moveNum] != ' ':
		print('The place is already filled.')
	else:
		gameboard[moveNum] = 'O'


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


def decideWinner(gameboard):
	global playerTurn
	global cpuTurn

	if playerTurn:
		if any(i == ' ' for i in gameboard.values()):
			print('\nAwww! You lost!')
		else:
			print('\nYou tie!')
		endingText()
	elif cpuTurn:
		if any(i == ' ' for i in gameboard.values()):
			print('\nCongratulations! You won!')
		else:
			print('\nYou tie!')
		endingText()

def updateGame(gameboard):
	global playerTurn
	global cpuTurn

	if cpuTurn:
		cpuBestMove(gameboard)
		printGameboard(gameboard)
		playerTurn = True
		cpuTurn = False
	elif playerTurn:
		playerMove(gameboard)
		printGameboard(gameboard)
		playerTurn = False
		cpuTurn = True


def main():
	global cpuTurn
	global playerTurn
	global board

	rand = random.randint(0,1)

	if rand:
		print('The computer moves first.')
		cpuTurn = True
	else:
		print('The player moves first.')
		playerTurn = True
	printGameboard(board)

	while not isGameOver(board):
		updateGame(board)
	decideWinner(board)

if __name__ == "__main__":
	main()