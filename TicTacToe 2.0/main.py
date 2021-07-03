import random

whoseTurn = 0 # Player's turn: 1,   AI's turn: -1 
MAX = 1
MIN = -1
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


def getAvailable(gameboard):
	availablePlaces = []
	for key, value in gameboard.items():
		if value == ' ':
			availablePlaces.append(key)
	return availablePlaces


def playerMove(moveNum):
	global board
	print('It\'s your turn now! Which place would you like to move to?')
	board[moveNum] = 'O'


def AIBestMove():
	global board
	gameboard = board.copy()
	depth = len(getAvailable(gameboard))
	print('\nComputer\'s move: ')

	if depth == 9:
		moveNum = random.randrange(1,10)
	else:
		bestMove = minimax(gameboard, depth, -1)
		moveNum = bestMove[0]
	board[moveNum] = 'X'


def minimax(gameboard, depth, turn):
	if turn == 1:
		bestMove = [-1, float('-inf')]
		move = 'O'
	else:
		bestMove = [-1, float('inf')]
		move = 'X'

	if depth == 0 or isGameOver(gameboard):
		return [-1, getScore(gameboard)]

	for i in getAvailable(gameboard):
		gameboard[i] = move
		moveScore = minimax(gameboard, depth, -turn)
		gameboard[i] = ' '
		bestMove[0] = i

		if turn == 1:
			if moveScore[1] > bestMove[1]:
				bestMove = moveScore # Get maximum value
		else:
			if moveScore[1] < bestMove[1]:
				bestMove = moveScore # Get minimum value
	return bestMove


def getScore(gameboard):
	# Game is over if all places are filled or the winBoard is matched
	# by 3 rows, 3 columns, or 2 diagonals
	winBoard = [
		[1, 2, 3], [4, 5, 6], [7, 8, 9],
		[1, 4, 7], [2, 5, 8], [3, 6, 9],
		[3, 5, 7], [1, 5, 9]
	]

	for w in winBoard:
		if gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] != ' ':
			if whoseTurn: # AI won
				return -1
			elif whoseTurn == -1: # Player won
				return 1
	if getAvailable(gameboard) == []:
		return 0


def isGameOver(gameboard):
	if getScore(gameboard) == None:
		return False
	elif getScore(gameboard) == -1:
		print('\nAwww! You lost!')
	elif getScore(gameboard) == 1:
		print('\nCongratulations! You won!')
	elif getScore(gameboard) == 0:
		print('\nYou tie!')
	return True


def updateGame():
	global whoseTurn
	
	# AI's turn
	if whoseTurn == -1: 
		AIBestMove()
		whoseTurn = 1
		printGameboard()
	
	# Player's turn
	elif whoseTurn:
		moveNum = int(input())
		if moveNum not in getAvailable(board):
			print('The place you choose to move is not available.')
		else:
			playerMove(moveNum)
			whoseTurn = -1
			printGameboard()


def endingText():
	print('\n--------------------')
	print('|    Game Over!    |')
	print('|                  |')
	print('| Thx for Playing! |')
	print('--------------------\n')


def main():
	global whoseTurn
	
	rand = random.randint(0,1)
	if rand:
		print('The computer moves first.')
		whoseTurn = -1
	else:
		print('The player moves first.')
		whoseTurn = 1
	printGameboard()

	while not isGameOver(board):
		updateGame()
	endingText()

if __name__ == "__main__":
	main()
