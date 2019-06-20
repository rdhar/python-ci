'''
Testing tic-tac-toe game.
'''

import random
import sys
import time
playingGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def numToText(num):
    '''
    Convert number input to equivalent characters.
    '''

    # If the array is labelled 0,
    # then it'll print out a blank/empty space

    if num == 0:
        return ' '

    # If the array is labelled 1,
    # then it'll print out a nought 'O'

    if num == 1:
        return 'O'

    # If the array is labelled 2,
    # then it'll print out a cross 'X'

    if num == 2:
        return 'X'


def printGrid():
    '''
    Render the tic-tac-toe grid.
    '''
    print '┌ ─ ┬ ─ ┬ ─ ┐'
    print '│ ' + numToText(playingGrid[0][0]) + ' │ ' \
        + numToText(playingGrid[1][0]) + ' │ ' \
        + numToText(playingGrid[2][0]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + numToText(playingGrid[0][1]) + ' │ ' \
        + numToText(playingGrid[1][1]) + ' │ ' \
        + numToText(playingGrid[2][1]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + numToText(playingGrid[0][2]) + ' │ ' \
        + numToText(playingGrid[1][2]) + ' │ ' \
        + numToText(playingGrid[2][2]) + ' │'
    print '└ ─ ┴ ─ ┴ ─ ┘'


def checkVictory():
    '''
    Looks at each box in the grid and checks 3 boxes in each specified
    vector.
    '''
    for i in range(0, 3):
        for j in range(0, 3):

            if playingGrid[i][j] == 0:
                continue

            # The 4 ways that the program will check for the 8 possibilities
            # of winning.
            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = playingGrid[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0]
                        boxToCheck[1] += vector[1]

                        # Checks for the same symbols in the vectors that form
                        # a complete line (so that if a line is complete, the
                        # endgame will run)
                        if playingGrid[boxToCheck[0]][boxToCheck[1]] \
                                != charToCheckFor:
                            break

                        # If last box in loop and still have not broken, then
                        # three in a row has been formed. print character

                        if x == 2:
                            return numToText(playingGrid[i][j])
                except:
                    continue
    return ' '


def chooseComputerMove():
    '''
    Let computer choose a valid move to play.
    '''

    emptyBoxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if playingGrid[i][j] == 0:
                # Creates a list of possibilities, picks at random from them.
                # Saves time on coding each and every single possibility, at
                # the cost of "smart" AI
                emptyBoxes += [[i, j]]
    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]


print 'Welcome to tic-tac-toe! Input coords in the form x y.\nEg, 1 1 or 2 1.'

# players move.

while 1:

    while 1:  # Repeat process until a valid input is detected and processed

        move = input('''

''')

        if len(move) == 3:
            # Check for correct input
            if 1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3:
                # Check that box is empty
                if playingGrid[int(move[0]) - 1][int(move[2]) - 1] == 0:
                    # Put a cross in box
                    playingGrid[int(move[0]) - 1][int(move[2]) - 1] = 2
                    printGrid()
                    break

            print 'Invalid input; try again with proper coords input format.'

    victoryResult = checkVictory()
    if victoryResult == 'X':
        print 'You win! :)'
        break  # Checks if the player has won

    computerMove = chooseComputerMove()
    playingGrid[computerMove[0]][computerMove[1]] = 1
    print '''

Computer\'s turn...'''
    printGrid()  # Makes the computer move

    victoryResult = checkVictory()
    if victoryResult == 'O':
        print 'You lose :('
        break  # Check if the computer has won
time.sleep(5)
sys.exit
