#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import time
playingGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def numToText(num):
    if num == 0:  # If the array is labelled 0, then it'll print out a blank/empty space
        return ' '
    if num == 1:  # If the array is labelled 1, then it'll print out a nought 'O'
        return 'O'
    if num == 2:  # If the array is labelled 2, then it'll print out a cross 'X'
        return 'X'

def printGrid():
    print ('┌ ─ ┬ ─ ┬ ─ ┐')
    print ('│ '
        + numToText(playingGrid[0][0]) + ' │ ' \
        + numToText(playingGrid[1][0]) + ' │ ' \
        + numToText(playingGrid[2][0]) + ' │')
    print ('├ ─ ┼ ─ ┼ ─ ┤')
    print ('│ '
        + numToText(playingGrid[0][1]) + ' │ ' \
        + numToText(playingGrid[1][1]) + ' │ ' \
        + numToText(playingGrid[2][1]) + ' │')
    print ('├ ─ ┼ ─ ┼ ─ ┤')
    print ('│ '
        + numToText(playingGrid[0][2]) + ' │ ' \
        + numToText(playingGrid[1][2]) + ' │ ' \
        + numToText(playingGrid[2][2]) + ' │')
    print ('└ ─ ┴ ─ ┴ ─ ┘')

def checkVictory():

    for i in range(0, 3):  # Looks at each box in the grid and checks 3 boxes in each specified vector
        for j in range(0, 3):

            if playingGrid[i][j] == 0:
                continue

            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:  # The 4 ways that the program will check for the 8 possibilities of winning.

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = playingGrid[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0]
                        boxToCheck[1] += vector[1]

                        if playingGrid[boxToCheck[0]][boxToCheck[1]] \
                            != charToCheckFor:  # Checks for the same symbols in the vectors that form a complete line (so that if a line is complete, the endgame will run)
                            break

                       # If last box in loop and still have not broken, then three in a row has been formed. print character
                        if x == 2:
                            return numToText(playingGrid[i][j])
                except:
                    continue
    return ' '

def chooseComputerMove():

    emptyBoxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if playingGrid[i][j] == 0:
                emptyBoxes += [[i, j]]  # Creates a list of possibilities, picks at random from them. Saves time on coding each and every single possibility, at the cost of "smart" AI
    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]

print('Welcome to tic-tac-toe! Input co-ords in the form x y.\nE.g., 1 1, 2 1 or 3 3.')

# players move.
while 1:

    while 1:  # Repeat process until a valid input is detected and processed

        move = input('\n\n')

        if len(move) == 3:
            if 1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3:  # Check for correct input
                if playingGrid[int(move[0]) - 1][int(move[2]) - 1] == 0:  # Check that box is empty
                    playingGrid[int(move[0]) - 1][int(move[2]) - 1] = 2  # Put a cross in box
                    printGrid()
                    break

            print ('Invalid input. Try again with proper co-ords')

    victoryResult = checkVictory()
    if victoryResult == 'X':
        print ('You win! :)')
        break  # Checks if the player has won

    computerMove = chooseComputerMove()
    playingGrid[computerMove[0]][computerMove[1]] = 1
    print ('\n\nComputer\'s turn...')
    printGrid()  # Makes the computer move

    victoryResult = checkVictory()
    if victoryResult == 'O':
        print ('You lose :(')
        break  # Check if the computer has won
time.sleep(5)
sys.exit
