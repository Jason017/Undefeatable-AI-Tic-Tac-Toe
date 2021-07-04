import random

whoseTurn = 0 # AI's turn: 1 ,  Player's turn: -1
AI = 1
PLAYER = -1
board = {
	1: ' ', 2: ' ', 3: ' ', 
	4: ' ', 5: ' ', 6: ' ', 
	7: ' ', 8: ' ', 9: ' '
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
	printGameboard()


def AIBestMove():
	global board
	gameboard = board.copy()
	depth = len(getAvailable(gameboard))
	print('\nAI\'s move: ')

	if depth == 9:
		moveNum = random.randrange(1,10)
	else:
		bestMove = minimax(gameboard, depth, AI)
		moveNum = bestMove[0]
	board[moveNum] = 'X'
	printGameboard()


def minimax(gameboard, depth, turn):
	if turn == AI:
		bestMove = [-1, float('-inf')] # Get maximum value for AI
		move = 'X'
	elif turn == PLAYER:
		bestMove = [-1, float('inf')] # Get minimum value for the player
		move = 'O'

	if depth == 0 or isGameOver(gameboard):
		return [-1, getScore(gameboard)]

	for i in getAvailable(gameboard):
		gameboard[i] = move
		moveScore = minimax(gameboard, depth, -turn)
		gameboard[i] = ' '
		moveScore[0] = i

		if turn == AI:
			if moveScore[1] > bestMove[1]:
				bestMove = moveScore # Get maximum value
		elif turn == PLAYER:
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
			if whoseTurn == AI: # Player won
				return -1
			elif whoseTurn == PLAYER: # AI won
				return 1
	if getAvailable(gameboard) == []:
		return 0


def isGameOver(gameboard):
	if getScore(gameboard) == None:
		return False
	return True


def updateGame():
	global whoseTurn
	
	# AI's turn
	if whoseTurn == AI:
		AIBestMove()
		whoseTurn = PLAYER
	# Player's turn
	elif whoseTurn == PLAYER:
		moveNum = int(input())
		if moveNum not in getAvailable(board):
			print('The place you choose to move is not available.')
		else:
			playerMove(moveNum)
			whoseTurn = AI


def endingText():
	if getScore(board) == 1:
		print('\nAwww! You lost!')
	elif getScore(board) == -1:
		print('\nCongratulations! You won!')
	elif getScore(board) == 0:
		print('\nYou tie!')
		
	print('\n--------------------')
	print('|    Game Over!    |')
	print('|                  |')
	print('| Thx for Playing! |')
	print('--------------------\n')


def main():
	global whoseTurn
	
	if random.randrange(2):
		print('AI moves first.')
		whoseTurn = AI
	else:
		print('Player moves first.')
		whoseTurn = PLAYER
	printGameboard()

	while not isGameOver(board):
		updateGame()
	endingText()

if __name__ == "__main__":
	main()
