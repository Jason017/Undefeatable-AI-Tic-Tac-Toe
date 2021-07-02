import random

playerTurn = False
cpuTurn = False
availablePlaces = list(range(1,10))
board = {
	1: ' ', 2: ' ', 3: ' ', 
	4: ' ', 5: ' ', 6: ' ', 
	7: ' ', 8: ' ', 9: ' ', 
}

def printGameboard():
	print()
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
	print('---+---+---')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
	print('---+---+---')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
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


def isGameOver():
	# Game is also over if all places are filled or the winBoard is matched
	# by 3 rows, 3 columns, or 2 diagonals
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
		if board[w[0]] == board[w[1]] == board[w[2]] != ' ':
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


def updateGame():
	global playerTurn
	global cpuTurn
	global board

	if cpuTurn:
		cpuRandomMove(board)
		printGameboard()
		playerTurn = True
		cpuTurn = False
	elif playerTurn:
		moveNum = int(input())
		if moveNum not in availablePlaces:
			print('The place you choose to move is not available.')
		else:
			playerMove(board, moveNum)
			printGameboard()
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
	
	rand = random.randint(0,1)

	if rand:
		print('The computer moves first.')
		cpuTurn = True
	else:
		print('The player moves first.')
		playerTurn = True
	printGameboard()

	while not isGameOver():
		updateGame()
	endingText()

if __name__ == "__main__":
	main()