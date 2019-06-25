from tictactoe import HumanPlayer
from tictactoe import Board
from tictactoe import ConsoleUI
from tictactoe import ComputerPlayer


# class TestConsoleUI():

#     def test_game_over(self):
#         board = Board()
#         ui = ConsoleUI(board)

#         assert ui.game_over() == "Game over"

#     def test_error_message(self):
#         board = Board()
#         ui = ConsoleUI(board)

#         assert ui.error_message("There is an error") == "There is an error"

#     def test_render_position_when_position_is_empty(self):
#         board = Board()
#         ui = ConsoleUI(board)

#         # The cells are numbered 1-9 so array index 4 equates to cell 5
#         assert ui.render_position(4) == "5"

#     def test_render_position_returns_symbol_when_position_is_not_empty(self):
#         board = Board()
#         ui = ConsoleUI(board)
#         player = ComputerPlayer(board)
#         player.symbol = 'X'
#         board.set_position(4, player)

#         assert ui.render_position(4) == 'X'


class TestBoard():
    def test_set_position(self):
        board = Board()
        computer_player = ComputerPlayer(board)

        assert board.set_position(4, computer_player) == computer_player

    def test_get_position(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(4, player)

        assert board.get_position(4) == player

    def test_position_is_empty(self):
        board = Board()

        assert board.position_is_empty(4) is True

    def test_position_is_not_empty(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(4, player)

        assert board.position_is_empty(4) is False

    def test_three_in_a_row(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(3, player)
        board.set_position(4, player)
        board.set_position(5, player)

        assert board.three_in_a_row(3, 4, 5) is True

    def test_is_not_three_in_a_row(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(2, player)
        board.set_position(4, player)
        board.set_position(5, player)

        assert board.three_in_a_row(3, 4, 5) is False

    def test_game_is_over(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(3, player)
        board.set_position(4, player)
        board.set_position(5, player)

        assert board.game_is_over() is True

    def test_game_is_not_over(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(3, player)
        board.set_position(4, player)
        board.set_position(8, player)

        assert board.game_is_over() is False

    def test_is_full(self):
        board = Board()
        player = ComputerPlayer(board)
        board.set_position(0, player)
        board.set_position(1, player)
        board.set_position(2, player)
        board.set_position(3, player)
        board.set_position(4, player)
        board.set_position(5, player)
        board.set_position(6, player)
        board.set_position(7, player)
        board.set_position(8, player)

        assert board.is_full() is True

    def test_is_not_full(self):
        board = Board()

        assert board.is_full() is False


class TestComputerPlayer():

    def test_choose_symbol_other_player_picks_x(self):
        board = Board()
        computer_player = ComputerPlayer(board)
        computer_player.choose_symbol(other_player_symbol='x')

        assert computer_player.symbol == "O"

    def test_choose_symbol_other_player_picks_o(self):
        board = Board()
        computer_player = ComputerPlayer(board)
        computer_player.choose_symbol(other_player_symbol='O')

        assert computer_player.symbol == "X"

    def test_get_symbol(self):
        board = Board()
        computer_player = ComputerPlayer(board)
        computer_player.symbol = "X"

        assert computer_player.get_symbol() == "X"

    def test_get_other_player_is_none(self):
        board = Board()
        player = ComputerPlayer(board)
        assert player.get_other_player() is None

    def test_get_other_player_when_position_not_empty(self):
        board = Board()
        ui = ConsoleUI(board)
        computer = ComputerPlayer(board)
        human = HumanPlayer(board, ui)
        board.set_position(4, computer)
        board.set_position(5, human)

        assert computer.get_other_player() == human


class TestHumanPlayer():

    def test_get_symbol(self):
        board = Board()
        ui = ConsoleUI(board)
        human_player = HumanPlayer(board, ui)
        human_player.symbol = "S"

        assert human_player.get_symbol() == "S"
