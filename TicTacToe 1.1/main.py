import random

playerTurn = False
cpuTurn = False
availablePlaces = list(range(1,10))
board = {
	1: ' ', 2: ' ', 3: ' ', 
	4: ' ', 5: ' ', 6: ' ', 
	7: ' ', 8: ' ', 9: ' ', 
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
	global availablePlaces
	print('\nComputer\'s move: ')

	randNum = random.choice(availablePlaces)
	gameboard[randNum] = 'X'
	availablePlaces.remove(randNum)


def playerMove(gameboard, moveNum):
	global availablePlaces
	print('It\'s your turn now! Which place would you like to move to?')
	
	gameboard[moveNum] = 'O'
	availablePlaces.remove(moveNum)


def isGameOver(gameboard):
	# Game is also over if all places are filled or the winBoard is matched
	# by 3 rows, 3 columns, or 2 diagonals
	global availablePlaces
	global playerTurn
	global cpuTurn

	winBoard = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9],
		[1, 4, 7],
		[2, 5, 8],
		[3, 6, 9],
		[3, 5, 7],
		[1, 5, 9]
	]

	for w in winBoard:
		if gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] != ' ':
			if playerTurn:
				print('\nAwww! You lost!')
				return True
			elif cpuTurn:
				print('\nCongratulations! You won!')
				return True
	if availablePlaces == []:
		print('\nYou tie!')
		return True
	return False


def updateGame(gameboard):
	global playerTurn
	global cpuTurn

	if cpuTurn:
		cpuRandomMove(gameboard)
		printGameboard(gameboard)
		playerTurn = True
		cpuTurn = False
	elif playerTurn:
		moveNum = int(input())
		if moveNum not in availablePlaces:
			print('The place you choose to move is not available.')
		else:
			playerMove(gameboard, moveNum)
			printGameboard(gameboard)
			playerTurn = False
			cpuTurn = True


def endingText():
	print('\n--------------------')
	print('|    Game Over!    |')
	print('|                  |')
	print('| Thx for Playing! |')
	print('--------------------\n')


def main():
	global playerTurn
	global cpuTurn
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
	endingText()

if __name__ == "__main__":
	main()