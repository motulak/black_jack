import unittest
from blackjack import *

class TestCards(unittest.TestCase):
    def test_check(self):
        return True

    def test_if_class_gracz(self):
        gracz = Player('TestPlayer')
        self.assertEqual(gracz.name, 'TestPlayer')
        self.assertEqual(gracz.cards, [])
        self.assertEqual(gracz.hit_me, True)
        self.assertEqual(gracz.in_game, True)