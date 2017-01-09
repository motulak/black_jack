#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest, random
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

    def add_card_to_player(self,player,(cards_ranks)):
        for rank in cards_ranks:
            card = Card(rank,random.choice(['spades','hearts','diamonds','clubs']))
            player.recive_card(card)

    def test_recive_cards(self):
        player1 = Player()
        self.add_card_to_player(player1,('1','2','3','4','5','6'))
        self.assertEqual(player1.cards.__len__(),6)


    def add_cards_to_player_and_check_thair_value(self, value, cards_ranks):
        player1 = Player()
        self.add_card_to_player(player1,cards_ranks)
        self.assertEqual(player1.return_cards_value(), value)

    def test_player_return_cards_value(self):
        self.add_cards_to_player_and_check_thair_value(11, ('1','10'))
        self.add_cards_to_player_and_check_thair_value(2, ('1', '1'))
        self.add_cards_to_player_and_check_thair_value(5, ('2', '3'))
        self.add_cards_to_player_and_check_thair_value(12, ('1', '2','3','6'))
        self.add_cards_to_player_and_check_thair_value(11, ('1', '10'))
        self.add_cards_to_player_and_check_thair_value(15, ('A', '4'))
        self.add_cards_to_player_and_check_thair_value(18, ('J', '8'))
        self.add_cards_to_player_and_check_thair_value(19, ('10', '9'))
        self.add_cards_to_player_and_check_thair_value(20, ('Q', 'K'))
        self.add_cards_to_player_and_check_thair_value(21, ('A', '10'))
        self.add_cards_to_player_and_check_thair_value(21, ('Q', 'Q','1'))
        self.add_cards_to_player_and_check_thair_value(21, ('A', '10','10'))
        self.add_cards_to_player_and_check_thair_value(22, ('A', '10','Q','A'))
        self.add_cards_to_player_and_check_thair_value(30, ('Q','K','J'))


    def test_decorator_user(self):
        player1 = Player()
        printer = Printer()
        self.assertEqual(printer.player_name(player1),'John Doe')
        card1 = Card('1','hearts')
        player1.recive_card(card1)
        self.assertEqual(printer.player_cards(player1), '| 1 ♥ |  ')
        card2 = Card('Q', 'clubs')
        player1.recive_card(card2)
        self.assertEqual(printer.player_cards(player1), '| 1 ♥ |  | Q ♣ |  ')
        card2 = Card('10', 'diamonds')
        player1.recive_card(card2)
        self.assertEqual(printer.player_cards(player1), '| 1 ♥ |  | Q ♣ |  |10 ♦ |  ')
        player2 = Player('Anna')
        self.assertEqual(printer.player_name(player2), 'Anna')


    def test_add_dummyp_players(self):
        kasyno = Casino()
        kasyno.add_dummy_players(3)
        self.assertEqual(kasyno.players.__len__(), 3)
        self.assertEqual(kasyno.players[0].name, 'Anna')
        self.assertEqual(kasyno.players[1].name, 'Bozydar')
        self.assertEqual(kasyno.players[2].name, 'Cecylia')


    def test_flow_of_casino_with_black_jack(self):
        kasyno = Casino()
        printer = Printer()
        kasyno.add_dummy_players(3)
        self.add_card_to_player(kasyno.players[0], ('1','1'))
        self.add_card_to_player(kasyno.players[1], ('10', '1'))
        self.add_card_to_player(kasyno.players[2], ('Q', 'A'))
        self.assertEqual(kasyno.players[0].cards.__len__(),2)
        self.assertEqual(kasyno.check_if_black_jack(), True)


    def test_flow_of_casino_no_black_jack(self):
        kasyno = Casino()
        printer = Printer()
        kasyno.add_dummy_players(3)
        self.add_card_to_player(kasyno.players[0], ('1', '1'))
        self.add_card_to_player(kasyno.players[1], ('10', '1'))
        self.add_card_to_player(kasyno.players[2], ('Q', 'A','A'))
        self.assertEqual(kasyno.players[0].cards.__len__(), 2)
        self.assertEqual(kasyno.check_if_black_jack(), False)

    def test_dealing_to_only_in_play_players(self):
        def test_flow_of_casino_no_black_jack(self):
            kasyno = Casino()
            printer = Printer()
            kasyno.add_dummy_players(3)






