from texttable import Texttable
ROWS = 6
COLUMNS = 7


class BoardException(Exception):
    """
    Error class for the Board
    """
    def __init__(self, message=''):
        self._message = message

    def __str__(self):
        return self._message


class Board:
    """
    Class used for defining the Board entity
    The Board is a 6 row, 7 column matrix initialized with the value 0 in each cell
    """
    def __init__(self):
        self._rows = ROWS
        self._columns = COLUMNS
        self._board = [[0 for column in range(self._columns)] for row in range(self._rows)]

    def __str__(self):
        """
        The string representation of the board, using Texttables
        :return: -
        """
        table = Texttable()
        '''
        The header represents the number of each column (from 1 to 7)
        Because the indices of our matrix start from 0, 
            when we add a chip to the first column, 
            we'll actually add it to the column 0 and so on.
        '''
        # Creating the header
        header = ['1', '2', '3', '4', '5', '6', '7']
        table.header(header)
        '''
        For each row in our matrix we create a list with the existent values from each cell
        Then, we add that list to our Texttable as a row, using .add_row()
        '''
        # We create a list of the elements from each row
        for row in range(0, self._rows):
            data = []
            for val in self._board[row][:]:
                data.append(val)
            # We add the list to our table
            table.add_row(data)
        # Using .draw(), the table will be automatically 'created', so that it resembles a matrix
        return table.draw()

    def clear(self):
        """
        Function used to re-initialise the Board
        Can be used for restarting the game
        :return: -
        """
        self._board = [[0 for column in range(self._columns)] for row in range(self._rows)]

    def add_chip(self, player, column):
        """
        Function that adds a Player's chip on the board, on the specified column
        :param player: The Player whose chip is to be added
        :param column: The column on which the chip will be placed
        :return: The row on which the chip was placed, an error if the column is full (no chip can be added)
        """
        row = -1
        # We first validate the column, to see whether we can place the chip or not
        if column < 0 or column > 6:
            raise BoardException("This column doesn't exist! Try again!")
        # We check each row of the column (bottom up -> from the row with the highest index, to the one with the lowest)
        # The chip is placed on the first free row of the column
        # The index of the row is also returned
        is_placed = False
        for row in range(ROWS-1, -1, -1):
            if self._board[row][column] == 0:
                self._board[row][column] = player.id
                is_placed = True
                return row
        # In the case there are no free rows on the column, an error is raised
        if is_placed is False:
            raise BoardException("Column already full! Try again!")

    def check_player_win(self, player):
        """
        Simple function that is used to check whether a Player has won the game or not
        :param player: The Player that will be checked
        :return: True of the Player has won, False otherwise
        """
        '''
        This method of checking is not a very efficient one, because it takes, on each case, every element of the matrix
        Another way of doing the checking could be checking from the last added chip in all four directions 
        To be more clear, one could check from the last added chip:
            - up and down (on the column) for the vertical case
            - left and right (on the row) for the horizontal case
            - on the diagonal going from bottom-left to top-right that contains the place where the last chip was added
            - the same way as the first diagonal, but this time checking on a top-left bottom-right direction
        '''
        # Because the matrix values consist of the Players' ID's, we check based on a Player's ID
        player_id = player.id

        # Checking if a Player won by placing four chips on the same row (the horizontal case)
        # We only go to COLUMNS-3, because that's the last column on which the horizontal case can occur
        for column in range(COLUMNS-3):
            for row in range(ROWS):
                # For a Player to win, the chips must be consecutive on the row
                if self._board[row][column] == player_id and self._board[row][column+1] == player_id and \
                        self._board[row][column+2] == player_id and self._board[row][column+3] == player_id:
                    return True

        # Checking if a Player won by placing four chips on the same column (the vertical case)
        # Similar to the horizontal case, we only go to ROWS-3, because that's the last row on which this case can occur
        for column in range(COLUMNS):
            for row in range(ROWS-3):
                # Again, the chips must be consecutive
                if self._board[row][column] == player_id and self._board[row+1][column] == player_id and \
                        self._board[row+2][column] == player_id and self._board[row+3][column] == player_id:
                    return True

        # The same principle is also applied to the diagonal cases

        # Checking if a Player won by placing four consecutive chips on the same diagonal (the 'main' diagonal case)
        # 'main' diagonal - going from top-left to bottom-right
        for column in range(COLUMNS-3):
            for row in range(ROWS-3):
                if self._board[row][column] == player_id and self._board[row+1][column+1] == player_id and \
                        self._board[row+2][column+2] == player_id and self._board[row+3][column+3] == player_id:
                    return True

        # Checking if a Player won by placing four consecutive chips on the same diagonal (the 'secondary' diagonal case)
        # 'secondary' diagonal - going from top-right to bottom-left
        for column in range(COLUMNS-3):
            for row in range(3, ROWS):
                if self._board[row][column] == player_id and self._board[row-1][column+1] == player_id and \
                        self._board[row-2][column+2] == player_id and self._board[row-3][column+3] == player_id:
                    return True
        # If none of the above cases reached the 'return True' instruction, it means that the player hasn't won yet
        # Therefore, this function will return False
        return False

    def check_board_full(self):
        """
        This function is used to check whether the board is full or not
        A board is full when all its elements are not the initial value 0
        :return: True if the board is full, False otherwise
        """
        # We initially assume that the board has no occupied spaces
        occupied = 0
        # Then, we check each element to see if its value is different to the initial one
        # If so, the counter is increased
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self._board[row][column] != 0:
                    occupied += 1
        # If the counter is equal to the number of elements of the board, it means the board is full
        # Because a Connect Four board has 6 rows and 7 columns, there are 42 elements on the board
        if occupied == 42:
            return True
        else:
            return False
