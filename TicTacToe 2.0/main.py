import random
from math import inf as infinity

whoseTurn = 0  # AI's turn: 1 ,  Player's turn: -1
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

    if depth == 9:
        moveNum = random.randrange(1, 10)
    else:
        bestMove = minimax(gameboard, depth, AI)
        moveNum = bestMove[0]
    board[moveNum] = 'X'
    whoseTurn = PLAYER
    printGameboard()


def minimax(gameboard, depth, turn):
    if turn == AI:
        bestMove = [-1, -infinity]  # Get maximum value for AI
        move = 'X'
    else:
        bestMove = [-1, infinity]  # Get minimum value for players
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
    # by 3 rows, 3 columns, or 2 diagonals
    winBoard = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [3, 5, 7], [1, 5, 9]
    ]

    for w in winBoard:
        if gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] == 'O':
            return -1
        elif gameboard[w[0]] == gameboard[w[1]] == gameboard[w[2]] == 'X':
            return 1
    if getAvailable(gameboard) == []:
        return 0


def isGameOver(gameboard):
    return getScore(gameboard) != None


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

    print('\n-----------------------')
    print('|      Game Over!     |')
    print('|                     |')
    print('| Thanks for Playing! |')
    print('-----------------------\n')


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
