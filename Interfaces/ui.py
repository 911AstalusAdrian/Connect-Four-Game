from Board.board import BoardException


class UI:
    """
    Class used for the UI of the game
    """
    def __init__(self, board, player_1, player_2):
        """
        The entities needed to initialise the game in its UI form: a Board and two Players
        :param board: The Board on which the game is player
        :param player_1: The first Player
        :param player_2: The second Player
        """
        self._board = board
        self._player_one = player_1
        self._player_two = player_2

    def start(self):
        """
        The loop based on which the game is played
        :return: -
        """
        done = False
        index = 0
        # The index is used to determine whose turn it is (index = 0 -> Player 1; index = 1 -> Player 2)
        while not done:
            # We first show the board
            print(str(self._board))
            print("\n")
            # Based on the index, we ask for a move from the corresponding Player
            # If the move is valid, it will be performed, otherwise an error message will be displayed and the Player will have another chance
            if index % 2 == 0:
                # The first Player is asked for an input (for the column number) and if the input is valid, the program will try and add a chip on the respective column
                try:
                    p1_choice = int(input("P1 choose a column (1-7): "))
                    # Because the columns are indexed from 0 to 6, but printed as 1 to 7, we have to decrease the number of the column given by the user
                    p1_choice -= 1
                    # If the column is valid, the move will be made
                    # If the Player won, the game ends
                    if self.p1_move(p1_choice) is True:
                        print("P1 won!")
                        print(str(self._board))
                        done = True
                # The possible occurring errors are caught here
                except BoardException as be:
                    print(be)
                    index -= 1
                except ValueError as ve:
                    print(ve)
                    index -= 1
            else:
                # The second Player is asked for an input (for the column number) and if the input is valid, the program will try and add a chip on the respective column
                p2_choice = int(input("P2 choose a column (1-7): "))
                p2_choice -= 1
                # If the column is valid, the move will be made
                # If the Player won, the game ends
                try:
                    if self.p2_move(p2_choice) is True:
                        print("P2 won!")
                        print(str(self._board))
                        done = True
                # The possible occurring errors are caught here
                except BoardException as be:
                    print(be)
                    index -= 1
                except ValueError as ve:
                    print(ve)
                    index -= 1
            # After each iteration, the index will change
            index += 1
            index %= 2

        # If the loop is exited, it means that the game ended, and the user will be asked if a restart of the game is wanted
        self.try_restart()

    def p1_move(self, choice):
        """
        Function used to make the move on the board based on the first Player's input
        :param choice: The column on which a chip is to be added
        :return: True if the Player won, false otherwise
        This function adds the chip and then checks if the Player won
        """
        self._board.add_chip(self._player_one, choice)
        if self._board.check_player_win(self._player_one) is True:
            return True
        return False

    def p2_move(self, choice):
        """
        Function used to make the move on the board based on the second Player's input
        :param choice: The column on which a chip is to be added
        :return: True if the Player won, false otherwise
        This function adds the chip and then checks if the Player won
        """
        self._board.add_chip(self._player_two, choice)
        if self._board.check_player_win(self._player_two) is True:
            return True
        return False

    def try_restart(self):
        """
        Function which restarts the game if the user wants to
        :return: -
        The function displays a message and asks for an input
        If the input is 'y' (from 'yes'), the game will be restarted (Board cleared and the 'start' loop function called)
        Otherwise, the program stops
        """
        restart = input("Restart? y|n ")
        if restart == 'y':
            self._board.clear()
            self.start()
