import pygame
from Board.board import BoardException
from Interfaces.GUI.design import GUIDesign


class GUI:
    def __init__(self, board, player_one, player_two):
        """
        Similar to the UI, the GUI version needs the Board and the two Players to start the game
        :param board: The Board
        :param player_one: First Player
        :param player_two: Second Player
        """
        self._current_player = 0
        # We initialise the Players in a list
        self._players = [player_one, player_two]
        self._board = board
        # We also initialise the interface, the Player starting being the first one from the list
        self._gui = GUIDesign(self._players[0])

    def loop(self):
        """
        The main loop of the GUI version
        :return: -
        """
        valid_keys = [1, 2, 3, 4, 5, 6, 7]  # A list of the valid keyboard inputs
        # Variables used to check different situations
        update_gui = False  # If the GUI needs to be updated
        done = False  # If the game is done
        player_won = False  # If a Player won
        # Variables initialised for a row and a column index
        row = -1
        column = -1
        while not done:
            # The game can go on as long as the board is not full
            if not self.full_board():
                update_gui = False
                # We check for the keyboard inputs
                for event in pygame.event.get():
                    # The case when the game is exited manually
                    if event.type == pygame.QUIT:
                        done = True
                    # The cases when the user pressed a key on the keyboard
                    elif event.type == pygame.KEYDOWN:
                        # In the case when a Player won, we check for the 'y' and 'n' keyboard inputs (n = 110 in ASCII, y = 121 in ASCII)
                        if player_won is True:
                            # 'n' key means that the game will not restart, therefore, the loop ends
                            if event.key == 110:
                                done = True
                            # 'y' key means that the game will restart, reinitialising the Board and the variables used for checks
                            elif event.key == 121:
                                player_won = False
                                done = False
                                self.restart()
                        else:
                            # We check if the keyboard input was a number from 1 to 7
                            # ASCII code of 1 is 49, that's why we get the column by subtracting 49
                            column = (event.key - 49)
                            # If we have a valid column, the program will try and add a chip
                            # If not, nothing will happen, the GUI will wait for a valid input
                            if column+1 in valid_keys:
                                # The program tries to add a chip, and checks for Player win
                                # If an error occurs, a message will be displayed
                                try:
                                    row = self.add_chip(column)
                                    if row > -1:
                                        player_won = self.check_player_win(self.get_current_player())
                                        update_gui = True
                                except BoardException as be:
                                    self._gui.draw_error(str(be))
                # The GUI will be updated accordingly (whether a Player won or not)
                if update_gui:
                    self._gui.draw_board(self.get_current_player(), row, column)
                    if player_won:
                        self._gui.draw_player_win(self.get_current_player())
                    else:
                        # After a move, the Players will 'switch'
                        self.switch_player()
                        self._gui.draw_player(self.get_current_player())
            else:
                # Message for when the game ends as a draw
                self._gui.draw_error("It's a draw!")

    def full_board(self):
        """
        Function used to check whether the Board is full or not
        :return: True if full, False otherwise
        """
        return self._board.check_board_full()

    def switch_player(self):
        """
        Function used to switch the Players' turn
        :return: -
        """
        self._current_player += 1
        self._current_player = self._current_player % 2

    def restart(self):
        """
        Function used to restart the game
        It clears the Board, and re-initialises the GUI
        :return:
        """
        self._board.clear()
        self._gui.initialise_screen(self.get_current_player())

    def add_chip(self, column):
        """
        Adds a chip on the specified column
        :param column: The column on which a chip has to be added
        :return: The row on which the chip was added (or an error)
        """
        # We firstly get the Player for which a chip must be added
        player = self.get_current_player()
        return self._board.add_chip(player, column)

    def check_player_win(self, player):
        """
        Function that checks if a certain Player won the game or not
        :param player: The player that is checked
        :return: True if the Player won, False otherwise
        """
        return self._board.check_player_win(player)

    def get_current_player(self):
        """
        Function to get the current Player from the lst of Players
        :return: The current Player
        """
        return self._players[self._current_player]
