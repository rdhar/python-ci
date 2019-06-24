#!/usr/bin/env python
from termcolor import colored
from itertools import cycle


class ConsoleUI:
    def __init__(self, board, color_output=True):
        self.board = board
        self._color_output = color_output

    def game_over(self):
        print("Game over")
        return "Game over"

    def ask_for_input(self, prompt, validfn, error_message, inputfn=input):
        """Ask user for input and wait until they give one which is valid.

        Run me with `python -m doctest -v game.py`.
        https://docs.python.org/2/library/doctest.html

        For the happy path a user gives a valid answer after bring prompted
        and no error message is printed.

        >>> ui = ConsoleUI(Board(), color_output=False)
        >>> ui.ask_for_input(
        ...     prompt='Give me a number:',
        ...     validfn=lambda s: s.isdigit(),
        ...     error_message='Not a number!',
        ...     inputfn=lambda: '1')
        Give me a number:
        '1'

        If a user gives an invalid input, this function will keep asking them
        for something until they give one for which validfn(input) is True. In
        this example 'not a number :)' is input first, which is not a digit, so
        an error is printed. Then '1337' is passed in which is a digit so the
        function returns it.

        >>> inputs = ['1337', 'not a number :)']
        >>> ui.ask_for_input(
        ...     prompt='Give me a number:',
        ...     validfn=lambda s: s.isdigit(),
        ...     error_message='Not a number!',
        ...     inputfn=inputs.pop)
        Give me a number:
        ERROR: Not a number!
        '1337'
        """
        print(prompt)
        while True:
            input = inputfn()
            if not validfn(input):
                self.error_message(error_message)
                continue
            return input

    def color_msg(self, msg, color, attrs=[]):
        if self._color_output:
            return colored(msg, color, attrs=attrs)
        else:
            return msg

    def error_message(self, error_message):
        print(self.color_msg('ERROR: ' + error_message, 'red'))
        return error_message

    def board_updated(self):
        for line in self._render_board():
            print(self._color_line(line))

    def _color_line(self, line):
        line = line.replace('X', self.color_msg('X', 'red', attrs=['bold']))
        line = line.replace('O', self.color_msg('O', 'green', attrs=['bold']))
        return line

    def render_position(self, position):
        if self.board.position_is_empty(position):
            return str(position + 1)
        else:
            player = self.board.get_position(position)
            return player.get_symbol()

    def _render_board(self):
        cells = " %s | %s | %s "
        divider = "===+===+==="
        lines = [
            cells % (self.render_position(0),
                     self.render_position(1),
                     self.render_position(2)),
            divider,
            cells % (self.render_position(3),
                     self.render_position(4),
                     self.render_position(5)),
            divider,
            cells % (self.render_position(6),
                     self.render_position(7),
                     self.render_position(8)),
        ]
        return lines


class Board:
    def __init__(self):
        self.board = [None] * 9

    def set_position(self, position, player):
        self.board[position] = player
        return self.board[position]

    def get_position(self, position):
        assert not self.position_is_empty(position)
        return self.board[position]

    def clone(self):
        clone = Board()
        clone.board = list(self.board)
        return clone

    def position_is_empty(self, position):
        return self.board[position] is None

    def player_would_win(self, position, player):
        board_copy = self.clone()
        board_copy.set_position(position, player)
        return board_copy.game_is_over()

    def three_in_a_row(self, a, b, c):
        a, b, c = map(lambda position: self.board[position], [a, b, c])
        return (a == b == c) and (a is not None)

    def game_is_over(self):
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]
        columns = [
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
        ]
        diagonals = [
            [0, 4, 8],
            [2, 4, 6],
        ]
        for a, b, c in lines + columns + diagonals:
            if self.three_in_a_row(a, b, c):
                return True
        return False

    def is_full(self):
        for position in range(9):
            if self.position_is_empty(position):
                return False
        return True


class ComputerPlayer:
    def __init__(self, board):
        self.board = board

    def choose_symbol(self, other_player_symbol=None):
        if other_player_symbol == 'X' or other_player_symbol == 'x':
            self.symbol = 'O'
        else:
            self.symbol = 'X'

    def get_symbol(self):
        return self.symbol

    def take_turn(self):
        position = self.get_best_position()
        print("The computer plays in position %d " % (position + 1))
        self.board.set_position(position, self)

    def get_best_position(self):
        # Pick the space with the most degrees of freedom.
        best_positions = []
        best_positions += [4]           # Middle is best.
        best_positions += [0, 2, 6, 8]  # Then the corners.
        best_positions += [1, 3, 5, 7]  # Then the cross.
        best_position = None
        for position in best_positions:
            if self.board.position_is_empty(position):
                if best_position is None:
                    best_position = position

                other_player = self.get_other_player()
                if other_player:
                    if self.board.player_would_win(position, other_player):
                        best_position = position

                if self.board.player_would_win(position, self):
                    best_position = position
                    return best_position
        return best_position

    def get_other_player(self):
        for position in range(9):
            if not self.board.position_is_empty(position):
                player = self.board.get_position(position)
                if player != self:
                    return player
        return None


class HumanPlayer:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def choose_symbol(self, other_player_symbol=None):
        def _validfn(user_input):
            if user_input in 'ox':
                user_input = user_input.upper()
            if other_player_symbol == user_input:
                self.ui.error_message('Same as other player symbol')
                return False
            if len(user_input) > 1:
                self.ui.error_message('Must be a single character')
                return False
            return True

        input = self.ui.ask_for_input(
            prompt="Pick a piece (X or O)",
            validfn=_validfn,
            error_message="That is not a valid piece, try again!")
        self.symbol = input.upper() if input in 'ox' else input

    def get_symbol(self):
        return self.symbol

    def take_turn(self):
        while True:
            input = self.ui.ask_for_input(
                prompt="Enter a position between 1 and 9:",
                validfn=lambda user_input: user_input in list("123456789"),
                error_message="Please enter a number between 1 and 9")
            position = int(input) - 1

            if not self.board.position_is_empty(position):
                self.ui.error_message(
                    "There is already a piece in %d" % position)
                continue

            self.board.set_position(position, self)
            return


class GameSetup:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def initialise_players(self):
        player1 = self._initialise_player(1)
        player2 = self._initialise_player(2, player1.get_symbol())
        return player1, player2

    def _initialise_player(self, number, other_player_symbol=None):
        valid = ["Computer", "computer", "c", "Human", "human", "h"]
        player_type = self.ui.ask_for_input(
            prompt="Select Player {0} type ('Human', 'human', 'h' or"
            " 'Computer', 'computer', 'c')".format(number),
            validfn=lambda user_input: user_input in valid,
            error_message="Invalid selection")

        if player_type in ["Human", "human", "h"]:
            player = HumanPlayer(self.board, self.ui)
        else:
            player = ComputerPlayer(self.board)

        player.choose_symbol(other_player_symbol=other_player_symbol)

        return player


class Game:
    def __init__(self):
        self.board = Board()
        self.ui = ConsoleUI(self.board)
        game_setup = GameSetup(self.board, self.ui)
        self.player1, self.player2 = game_setup.initialise_players()

    def start_game(self):
        self.ui.board_updated()

        for player in cycle([self.player1, self.player2]):
            player.take_turn()
            self.ui.board_updated()
            if self.board.game_is_over():
                break
            if self.board.is_full():
                break
        self.ui.game_over()


if __name__ == '__main__':
    game = Game()
    game.start_game()
