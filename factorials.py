'''
Generate factorials.
'''

import sys


def fact(user_input):
    '''
    Factorial function

    :arg n: number
    :returns: factorial of n
    '''

    if user_input == 0:
        return 1
    return user_input * fact(user_input - 1)


def div(user_input):
    '''
    Just divide
    '''

    res = 10 / user_input
    return res


def main(user_input):
    '''
    Print results
    '''
    res = fact(user_input)
    print res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
