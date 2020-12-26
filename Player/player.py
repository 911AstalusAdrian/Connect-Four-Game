class Player:
    """
    Class used for defining the Player entity
    A Player only has an ID and, based on that ID, other attributes needed for the GUI, such as color and name
    The ID is used directly in the UI, when a chip is represented by the Player's ID
    In the case of the GUI, the players will be automatically created as having the ID's 1 and 2
    """

    def __init__(self, player_id):
        self._id = player_id

    @property
    def id(self):
        return self._id

    @property
    def color(self):
        if self._id == 1:
            return 255, 0, 0  # RGB code for colour red
        else:
            return 255, 255, 0  # RGB code for colour yellow

    @property
    def name(self):
        if self._id == 1:
            return "Red"
        else:
            return "Yellow"
