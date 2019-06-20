'''
Testing tic-tac-toe game.
'''

import random
import sys
import time
playing_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def num_to_text(num):
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


def print_grid():
    '''
    Render the tic-tac-toe grid.
    '''
    print '┌ ─ ┬ ─ ┬ ─ ┐'
    print '│ ' + num_to_text(playing_grid[0][0]) + ' │ ' \
        + num_to_text(playing_grid[1][0]) + ' │ ' \
        + num_to_text(playing_grid[2][0]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + num_to_text(playing_grid[0][1]) + ' │ ' \
        + num_to_text(playing_grid[1][1]) + ' │ ' \
        + num_to_text(playing_grid[2][1]) + ' │'
    print '├ ─ ┼ ─ ┼ ─ ┤'
    print '│ ' + num_to_text(playing_grid[0][2]) + ' │ ' \
        + num_to_text(playing_grid[1][2]) + ' │ ' \
        + num_to_text(playing_grid[2][2]) + ' │'
    print '└ ─ ┴ ─ ┴ ─ ┘'


def check_victory():
    '''
    Looks at each box in the grid and checks 3 boxes in each specified
    vector.
    '''
    for i in range(0, 3):
        for j in range(0, 3):

            if playing_grid[i][j] == 0:
                continue

            # The 4 ways that the program will check for the 8 possibilities
            # of winning.
            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:

                try:
                    box_to_check = [i, j]
                    char_to_check_for = playing_grid[i][j]
                    for x in range(1, 3):

                        box_to_check[0] += vector[0]
                        box_to_check[1] += vector[1]

                        # Checks for the same symbols in the vectors that form
                        # a complete line (so that if a line is complete, the
                        # endgame will run)
                        if playing_grid[box_to_check[0]][box_to_check[1]] \
                                != char_to_check_for:
                            break

                        # If last box in loop and still have not broken, then
                        # three in a row has been formed. print character

                        if x == 2:
                            return num_to_text(playing_grid[i][j])
                except:
                    continue
    return ' '


def choose_computer_move():
    '''
    Let computer choose a valid move to play.
    '''

    empty_boxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if playing_grid[i][j] == 0:
                # Creates a list of possibilities, picks at random from them.
                # Saves time on coding each and every single possibility, at
                # the cost of "smart" AI
                empty_boxes += [[i, j]]
    return empty_boxes[random.randint(1, len(empty_boxes) - 1)]


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
                if playing_grid[int(move[0]) - 1][int(move[2]) - 1] == 0:
                    # Put a cross in box
                    playing_grid[int(move[0]) - 1][int(move[2]) - 1] = 2
                    print_grid()
                    break

            print 'Invalid input; try again with proper coords input format.'

    victory_result = check_victory()
    if victory_result == 'X':
        print 'You win! :)'
        break  # Checks if the player has won

    computer_move = choose_computer_move()
    playing_grid[computer_move[0]][computer_move[1]] = 1
    print '''

Computer\'s turn...'''
    print_grid()  # Makes the computer move

    victory_result = check_victory()
    if victory_result == 'O':
        print 'You lose :('
        break  # Check if the computer has won
time.sleep(5)
sys.exit
