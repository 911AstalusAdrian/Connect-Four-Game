import unittest
from Player.player import Player


class TestPlayerEntity(unittest.TestCase):
    def setUp(self):
        self._player_one = Player(1)
        self._player_two = Player(5)

    def test_properties(self):
        self.assertEqual(self._player_one.id, 1)
        self.assertEqual(self._player_two.id, 5)
        self.assertEqual(self._player_one.color, (255,0,0))
        self.assertEqual(self._player_two.color, (255,255,0))
        self.assertEqual(self._player_one.name, "Red")
        self.assertEqual(self._player_two.name, "Yellow")