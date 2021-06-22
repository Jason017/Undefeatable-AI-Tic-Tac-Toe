import random


def printGameboard(gameboard):
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
		if board[i] == ' ':
			available.append(i)
	
	randChoice = random.choice(available)
	gameboard[randChoice] = 'X'
	printGameboard(gameboard)


def playerMove(gameboard):
	print('It\'s your turn now! Which place would you like to move to?')
	num = int(input())

	if gameboard[num] != ' ':
		print('The place is already filled.')
	else:
		gameboard[num] = 'O'


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


def decideFirstMove():
	rand = random.randint(0,1)
	if rand:
		print('The computer moves first.')
		cpuTurn = True
	else:
		print('The player moves first.')
		playerTurn = True


def decideWinner(gameboard, cpuTurn, playerTurn):
	if playerTurn:
		if all(i != ' ' for i in gameboard.values()):
			print('\nYou tie!')
		else:
			print('\nAwww! You lost!')
		endingText()
	elif cpuTurn:
		if all(i != ' ' for i in gameboard.values()):
			print('\nYou tie!')
		else:
			print('\nCongratulations! You won!')
		endingText()


def updateGame(gameboard, cpuTurn, playerTurn):
	if cpuTurn:
		cpuRandomMove(gameboard)
		cpuTurn = False
		playerTurn = True
	elif playerTurn:
		playerMove(gameboard)
		cpuTurn = True
		playerTurn = False


def main():
	cpuTurn = False
	playerTurn = False
	board = {
		1: ' ', 2: ' ', 3: ' ', 
		4: ' ', 5: ' ', 6: ' ', 
		7: ' ', 8: ' ', 9: ' ', 
	}
	decideFirstMove()
	printGameboard(board)

	while not isGameOver(board):
		updateGame(board, cpuTurn, playerTurn)
	decideWinner(board, cpuTurn, playerTurn)

if __name__ == "__main__":
	main()