import pygame

CHIP_SIZE = 80
OFFSET = 60
CHIP_OFFSET = 20
BOARD_HEIGHT = 200
CHIP_RADIUS = int(CHIP_SIZE / 2)


class GUIDesign:
    def __init__(self, player):
        # initialising Pygame module
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Connect Four (Python Edition)")  # Adding a caption
        self._screen = pygame.display.set_mode((800, 800))  # Setting the size of the board
        self._board_image = pygame.image.load(
            r"D:\FP\a11-911AstalusAdrian\images\board.png")  # The path of where your image is stored
        self._board_image_numbers = pygame.image.load(
            r"D:\FP\a11-911AstalusAdrian\images\board_numbers.png")  # The path of where your image is stored
        self._font = pygame.font.SysFont('Calibri', 26)
        self.initialise_screen(player)

    def initialise_screen(self, player):
        self._screen.fill((255, 255, 255))
        self.draw_board()
        self.draw_player(player)

    def draw_player_win(self, player):
        """
        Displaying a message when a certain player wins
        :param player: The player that won the game
        :return: -
        We create a rectangle in which we put a win message, then we 'update' the game
        """
        pygame.draw.rect(self._screen, (255, 255, 255), [0, 0, 800, 50], 0)
        '''
        self._screen is the 'place' where the rectangle will be placed
        the second parameter is the color of the rectangle in RGB (in this case black
        the third parameter contains the offset where the rectangle will be placed and its dimension
            - [0, 0] means that it will be placed in the top left corner
            - [800, 50] means that its width will be 800 and height will be 50
        the last parameter is used for line thickness or to indicate that the rectangle is to be filled   
        '''
        text = player.name + " won! Restart (y | n)?"
        text = self._font.render(text, True, (0, 0, 0))
        '''
        render() is used to draw the text on a surface
        the first parameter is the text to be rendered (can only be a single line)
        the second parameter is for antialiasing
        the third parameter is the colour of the text
        '''
        self._screen.blit(text, (50, 10))
        '''
        we use blit() to draw the surface of the text on the surface of self._screen
        the tuple (50, 10) is used to specify the dimensions of the second surface
        '''
        pygame.display.flip()

    def draw_player(self, player):
        """
        Function similar to draw_player_win
        :param player: the player to draw
        :return: -
        """
        pygame.draw.rect(self._screen, (255, 255, 255), [0, 0, 800, 50], 0)
        text = "Current player: " + player.name
        text = self._font.render(text, True, (0, 0, 0))
        self._screen.blit(text, (50, 10))
        pygame.display.flip()

    def draw_board(self, player=None, row=-1, column=-1):
        """
        Function used to 'add' a chip on the board
        :param player: The Player who adds the chip
        :param row: The index of the row
        :param column: The index of the column
        :return: -
        This function is also used to initialise the board interface, case in which the Player will be None
        """
        if player is not None:
            pygame.draw.circle(self._screen, player.color,
                               (OFFSET + CHIP_RADIUS + CHIP_OFFSET * column + CHIP_SIZE * column,
                                600 + CHIP_SIZE * (row - 5) + CHIP_OFFSET * (row - 5)), CHIP_RADIUS)
        self._screen.blit(self._board_image, (50, 50))
        self._screen.blit(self._board_image_numbers, (90, 650))
        pygame.display.flip()

    def draw_error(self, message):
        """
        Function used to display an error on the interface
        :param message: The message of the error
        :return: -
        """
        pygame.draw.rect(self._screen, (255, 255, 255), [0, 0, 800, 50], 0)
        text = self._font.render(message, True, (0, 0, 0))
        self._screen.blit(text, (50, 10))
        pygame.display.flip()
