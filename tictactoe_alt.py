# GLOBAL VARIABLES
M = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

S = True
C = 0


# FUNCTIONS
def board_show():
    print()
    for y in range(3):
        print(" ", end="")
        for x in range(3):
            print(M[y][x], end=" ")
        print()
    print()


def check_hr(y):
    return M[y][0] == M[y][1] == M[y][2] != '-'


def check_vr(x):
    return M[0][x] == M[1][x] == M[2][x] != '-'


def check_dig():
    return M[0][0] == M[1][1] == M[2][2] != '-' or \
        M[0][2] == M[1][1] == M[2][0] != '-'


def big_check():
    win = False
    for i in range(3):
        if check_hr(i) or check_vr(i):
            win = True
    if check_dig():
        win = True
    return win


def turn():
    global S, C
    pos = [(int(i) - 1) for i in input("Your move: ").split()]
    x, y = pos[0], pos[1]
    if M[y][x] == '-':
        M[y][x] = 'X' if S else 'O'
        S = not S
        C += 1
        board_show()
    else:
        print("Invalid move!")


# MAIN
def xo():
    board_show()
    while C < 9:
        turn()
        if big_check():
            print(f"{'X' if not S else 'O'} wins!", end="\n\n")
            break
    else:
        print("It's a tie!", end="\n\n")


xo()
