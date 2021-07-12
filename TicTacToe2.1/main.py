import random
from math import inf as infinity

whoseTurn = 0 # AI's turn: 1 ,  Player's turn: -1
AI = 1
PLAYER = -1
board = {
	1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 
	6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ',
	11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
	16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
	21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ',
}

def printGameboard():
	print()
	for i in range(5):
		n = i*5
		print(' ' + board[n+1] + ' | ' + board[n+2] + ' | ' + board[n+3] + ' | ' + board[n+4] + ' | ' + board[n+5] + ' ')
		if i != 4:
			print('---+---+---+---+---')
	print()


def getAvailable(gameboard):
	return [key for key, val in gameboard.items() if val == " "]


def playerMove():
	global board
	global whoseTurn

	print('It\'s your turn now! Which place would you like to move to?')
	
	moveNum = int(input())
	while moveNum not in getAvailable(board):
		print('The place you choose to move is not available.')
		moveNum = int(input())
	
	board[moveNum] = 'O'
	whoseTurn = AI
	printGameboard()


def AIBestMove():
	global board
	global whoseTurn
	
	print('\nAI\'s move: ')

	gameboard = board.copy()
	depth = len(getAvailable(gameboard))

	if depth == 25:
		moveNum = random.randrange(1,26)
	else:
		bestMove = minimax(gameboard, depth, AI)
		moveNum = bestMove[0]
	board[moveNum] = 'X'
	whoseTurn = PLAYER
	printGameboard()


def minimax(gameboard, depth, turn):
	if turn == AI:
		bestMove = [-1, -infinity] # Get maximum value for AI
		move = 'X'
	else:
		bestMove = [-1, infinity] # Get minimum value for players
		move = 'O'
	if depth == 0 or isGameOver(gameboard):
		return [-1, getScore(gameboard)]

	for i in getAvailable(gameboard):
		gameboard[i] = move
		moveScore = minimax(gameboard, depth - 1, -turn)
		gameboard[i] = ' '
		moveScore[0] = i

		if turn == AI:
			if moveScore[1] > bestMove[1]:
				bestMove = moveScore
		else:
			if moveScore[1] < bestMove[1]:
				bestMove = moveScore
	return bestMove

def getScore(gameboard):
	# Game is over if all places are filled or the winBoard is matched
	# by 5 rows, 5 columns, or 2 diagonals
	winBoard = [[1, 7, 13, 19, 25], [5, 9, 13, 17, 21]]
	for i in range(5):
		rows = list(range(1,6))
		cols = list(range(1,22,5))
		for j in range(5):
			rows[j] += i*5
			cols[j] += i
		winBoard.append(rows)
		winBoard.append(cols)

	for w in winBoard:
		if gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] == gameboard[w[3]] == gameboard[w[4]] == 'O':
			return -1
		elif gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] == gameboard[w[3]] == gameboard[w[4]] == 'X':
			return 1
	if getAvailable(gameboard) == []:
		return 0


def isGameOver(gameboard):
	if getScore(gameboard) == None:
		return False
	return True


def updateGame():
	if whoseTurn == AI:
		AIBestMove()
	elif whoseTurn == PLAYER:
		playerMove()


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
	getScore(board)
	while not isGameOver(board):
		updateGame()
	endingText()

if __name__ == "__main__":
	main()
