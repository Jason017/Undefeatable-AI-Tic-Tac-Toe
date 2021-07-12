# Tic Tac Toe 1.0
A preliminary python program playing Tic Tac Toe with the computer taking random moves.

# Tic Tac Toe 1.1
Commited some slight changes to simplify the function and made it easier to read.

```Python
board = {
	1: ' ', 2: ' ', 3: ' ', 
	4: ' ', 5: ' ', 6: ' ', 
	7: ' ', 8: ' ', 9: ' ', 
}
```

- Using a dictionary to store the data of the gameboard and count the winning format.
- Global variable `playerTurn` and `cpuTurn` to determine who's playing and who's winning the game eventually.

# Tic Tac Toe 2.0
Comprehensively upgraded Tic Tac Toe AI in python that no one can beat. You will probably have a tie, but only if you take careful strategy.

- Minimax Algorithm introduced by the concept of [game tree](https://en.wikipedia.org/wiki/Game_tree)

The implemented function:
```Python
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
```
