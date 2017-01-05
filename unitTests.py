import unittest
from blackjack import *

class TestCards(unittest.TestCase):
    def test_check(self):
        return True


    def assert_card_value(self, rank, suite, value):
        card = Card(rank, suite)
        self.assertEqual(card.rank, rank)
        self.assertEqual(card.suite, suite)
        self.assertEqual(card.return_value(), value)

    def test_creating_card(self):
        self.assert_card_value('1', 'spades', 1)
        self.assert_card_value('2', 'hearts', 2)
        self.assert_card_value('3', 'diamonds', 3)
        self.assert_card_value('4', 'clubs', 4)
        self.assert_card_value('5', 'spades', 5)
        self.assert_card_value('6', 'hearts', 6)
        self.assert_card_value('7', 'diamonds', 7)
        self.assert_card_value('8', 'clubs', 8)
        self.assert_card_value('9', 'spades', 9)
        self.assert_card_value('10', 'spades', 10)
        self.assert_card_value('J', 'hearts', 10)
        self.assert_card_value('Q', 'diamonds', 10)
        self.assert_card_value('K', 'spades', 10)
        self.assert_card_value('A', 'clubs', 11)

    def test_deck_new_deck(self):
        deck1 = Deck()
        player1 = Player('AAA')
        player2 = Player('BBB')
        player3 = Player('CCC')
        self.assertEqual(deck1.cards.__len__(), 52)
        card1 = Card('2', 'clubs')
        deck1.add_to_deck(card1)
        self.assertEqual(deck1.cards.__len__(), 53)
        deck1.give_card_to(card1, player1)
        self.assertEqual(deck1.cards.__len__(), 52)
        self.assertEqual(player1.cards.__len__(), 1)
        deck1.give_cards((player2, player3,), 26)
        self.assertEqual(player2.cards.__len__(), 26)
        self.assertEqual(player2.cards.__len__(), 26)
        self.assertEqual(deck1.cards.__len__(), 0)

    def test_if_class_gracz(self):
        gracz = Player('TestPlayer')
        self.assertEqual(gracz.name, 'TestPlayer')
        self.assertEqual(gracz.cards, [])
        self.assertEqual(gracz.hit_me, True)
        self.assertEqual(gracz.in_game, True)