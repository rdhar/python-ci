#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Testing tic-tac-toe game.
'''

import random
PLAYING_GRID = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def num_to_text(num):
    '''
    Convert number input to equivalent characters.
    '''

    # If the array is labelled 0,
    # then it'll print out a blank/empty space

    if num == 0:
        char_space = ' '
        return char_space

    # If the array is labelled 1,
    # then it'll print out a nought 'O'

    if num == 1:
        return 'O'

    # If the array is labelled 2,
    # then it'll print out a cross 'X'

    if num == 2:
        return 'X'


def print_grid():
    '''
    Render the tic-tac-toe grid.
    '''
    print '┌ ─ ┬ ─ ┬ ─ ┐'
    print '│ ' + num_to_text(PLAYING_GRID[0][0]) + ' │ ' \
        + num_to_text(PLAYING_GRID[1][0]) + ' │ ' \
        + num_to_text(PLAYING_GRID[2][0]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + num_to_text(PLAYING_GRID[0][1]) + ' │ ' \
        + num_to_text(PLAYING_GRID[1][1]) + ' │ ' \
        + num_to_text(PLAYING_GRID[2][1]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + num_to_text(PLAYING_GRID[0][2]) + ' │ ' \
        + num_to_text(PLAYING_GRID[1][2]) + ' │ ' \
        + num_to_text(PLAYING_GRID[2][2]) + ' │'
    print '└ ─ ┴ ─ ┴ ─ ┘'


def check_victory():
    '''
    Looks at each box in the grid and checks 3 boxes in each specified
    vector.
    '''
    for i in range(0, 3):
        for j in range(0, 3):

            if PLAYING_GRID[i][j] == 0:
                continue

            # The 4 ways that the program will check for the 8 possibilities
            # of winning.
            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:

                try:
                    box_to_check = [i, j]
                    char_to_check_for = PLAYING_GRID[i][j]
                    for k in range(1, 3):

                        box_to_check[0] += vector[0]
                        box_to_check[1] += vector[1]

                        # Checks for the same symbols in the vectors that form
                        # a complete line (so that if a line is complete, the
                        # endgame will run)
                        if PLAYING_GRID[box_to_check[0]][box_to_check[1]] \
                                != char_to_check_for:
                            break

                        # If last box in loop and still have not broken, then
                        # three in a row has been formed. print character

                        if k == 2:
                            return num_to_text(PLAYING_GRID[i][j])
                except SyntaxError:
                    continue
    return ' '


def choose_computer_move():
    '''
    Let computer choose a valid move to play.
    '''

    empty_boxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if PLAYING_GRID[i][j] == 0:
                # Creates a list of possibilities, picks at random from them.
                # Saves time on coding each and every single possibility, at
                # the cost of "smart" AI
                empty_boxes += [[i, j]]
    return empty_boxes[random.randint(1, len(empty_boxes) - 1)]


print 'Welcome to tic-tac-toe! Input coords in the form x y.\nEg, 1 1 or 2 1.'

# players move.

while 1:

    while 1:  # Repeat process until a valid input is detected and processed

        MOVE = input('''

''')

        if len(MOVE) == 3:
            # Check for correct input
            if 1 <= int(MOVE[0]) <= 3 and 1 <= int(MOVE[2]) <= 3:
                # Check that box is empty
                if PLAYING_GRID[int(MOVE[0]) - 1][int(MOVE[2]) - 1] == 0:
                    # Put a cross in box
                    PLAYING_GRID[int(MOVE[0]) - 1][int(MOVE[2]) - 1] = 2
                    print_grid()
                    break

            print 'Invalid input; try again with proper coords input format.'

    VICTORY_RESULT = check_victory()
    if VICTORY_RESULT == 'X':
        print 'You win! :)'
        break  # Checks if the player has won

    COMPUTER_MOVE = choose_computer_move()
    PLAYING_GRID[COMPUTER_MOVE[0]][COMPUTER_MOVE[1]] = 1
    print '''

Computer\'s turn...'''
    print_grid()  # Makes the computer move

    VICTORY_RESULT = check_victory()
    if VICTORY_RESULT == 'O':
        print 'You lose :('
        break  # Check if the computer has won
