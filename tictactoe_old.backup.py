import random
import sys

#### Initialising ####

boxes = [[0, 0, 0],  # 0 - empty
         [0, 0, 0],  # 1 - nought
         [0, 0, 0]]  # 2 - cross

#### Functions ####

# Converts the box's magic number into a character


def intToText(num):
    if (num == 0):
        return ' '
    if (num == 1):
        return 'O'
    if (num == 2):
        return 'X'

# This outputs the grid, with the correct symbols in the boxes


def printGrid():
    print('┌─┬─┬─┐' '\n'
          '│' + intToText(boxes[0][0]) + '│' + intToText(boxes[1]
                                                         [0]) + '│' + intToText(boxes[2][0]) + '│' '\n'
          '├─┼─┼─┤' '\n'
          '│' + intToText(boxes[0][1]) + '│' + intToText(boxes[1]
                                                         [1]) + '│' + intToText(boxes[2][1]) + '│' '\n'
          '├─┼─┼─┤' '\n'
          '│' + intToText(boxes[0][2]) + '│' + intToText(boxes[1]
                                                         [2]) + '│' + intToText(boxes[2][2]) + '│' '\n'
          '└─┴─┴─┘')


def checkVictory():

    # This method looks at each box in the grid and checks the two boxes
    # in each of the four directions defined as vectors below

    for i in range(0, 3):
        for j in range(0, 3):

            if (boxes[i][j] == 0):
                continue

            # The four directions to check for a complete line in
            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = boxes[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0]
                        boxToCheck[1] += vector[1]

                        # Check if the box contains the same symbol as the previous ones in the line
                        if (boxes[boxToCheck[0]][boxToCheck[1]] != charToCheckFor):
                            break

                        # If we're on the last box in the loop and haven't broken out yet,
                        # we've found 3 in a row. Return the character in the box.
                        if (x == 2):
                            return intToText(boxes[i][j])

                except:
                    continue
    return ' '


def chooseComputerMove():

    # This just fills a list with all the empty boxes and chooses one at random
    emptyBoxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if (boxes[i][j] == 0):
                emptyBoxes += [[i, j]]

    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]

#### Program ####


input('Welcome to noughts and crosses! Press enter to start.')

print('\n' 'You are playing as crosses')
printGrid()

while(1):

    while(1):  # Loop until valid input is entered

        move = input('\n' 'Your turn. Make your move:' '\n')

        if (move == 'help'):
            print('Type the coordinates (originating from the top left) of the box you want to put a cross into in the format \'x y\' (e.g. 3 2)')
            print('')
            continue

        if (len(move) == 3):
            # Check the user has entered valid coordinates
            if (1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3):
                # Check that the chosen box is empty
                if (boxes[int(move[0]) - 1][int(move[2]) - 1] == 0):
                    boxes[int(move[0]) - 1][int(move[2]) -
                                            1] = 2  # Put an X in the box
                    printGrid()
                    break

        print('Invalid input. Type \'help\' if you\'re stuck')

    # Check if the player's move won the game
    victoryResult = checkVictory()
    if (victoryResult == 'X'):
        print ('You win!')
        break

    # Make the computer's move
    computerMove = chooseComputerMove()
    boxes[computerMove[0]][computerMove[1]] = 1
    print('\n' 'Computer\'s turn:')
    printGrid()

    # Check if the computer's move won the game
    victoryResult = checkVictory()
    if (victoryResult == 'O'):
        print ('Computer wins!')
        break

sys.exit
