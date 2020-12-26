from Interfaces.ui import UI
from Interfaces.GUI.gui import GUI
from Board.board import Board
from Player.player import Player

# We initialise the Board
game_board = Board()
# We ask the user to choose between UI and GUI
interface = input("\nChoose between UI and GUI: ")
interface.lower()
if interface == 'ui':
    # For UI, Player IDs are required
    # The IDs must be different numbers
    try:
        player1_value = int(input("Choose a number for P1: "))
        player2_value = int(input("Choose a number for P2: "))
        if player2_value != player1_value:
            player_1 = Player(player1_value)
            player_2 = Player(player2_value)
            ui = UI(game_board, player_1, player_2)
            ui.start()
        else:
            print("Identical values given! ")
    except ValueError as ve:
        print(ve)
elif interface == 'gui':
    # For GUI, the IDs are automatically set as 1 and 2
    player_1 = Player(1)
    player_2 = Player(2)
    gui = GUI(game_board, player_1, player_2)
    gui.loop()
else:
    print("Invalid Choice!")
