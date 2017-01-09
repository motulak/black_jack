#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

""" spades (♠), hearts (♥), diamonds (♦) and clubs (♣)"""

class Casino(object):

    def __init__(self):
        self. BLACK_JACK = 21
        self.players = []
        self.deck = Deck()


    def add_dummy_players(self,number_of_players):
        self.dummy_names = ['Anna','Bozydar','Cecylia','Drago','Elżbieta','Felicjan','Grażyna','Hieronim','Irmina','Józef']
        if number_of_players > 10:
            number_of_players = 10
            print "Max players is 10"
        for x in range(number_of_players):
            player = Player(self.dummy_names[x])
            self.players.append(player)

    def deal_the_cards_for_in_game_players(self,number_of_cars):
        current_round_players = []
        for player in self.players:
            if player.in_game():
                current_round_players.append(player)
        self.deck.give_cards(current_round_players,2)

    def check_if_black_jack(self):
        black_jack = False
        for player in self.players:
            if player.return_cards_value() == self.BLACK_JACK:
                black_jack = True
            else: black_jack = False
        return black_jack

class Card(object):
    def __init__(self,rank,suite):
        self.rank = rank
        self.suite = suite

    def return_value(self):
        value = 0
        if self.rank not in ('J', 'Q', 'K', 'A'):
            value = int(self.rank)
        elif self.rank in ('J', 'Q', 'K'):
                value = 10
        elif self.rank == 'A':
            value = 11
        return value


class Deck(object):
    suites = ['spades','hearts','diamonds','clubs']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def __init__(self):
        self.cards = []
        self.new()
        self.shuffle()

    def new(self):
        for suite in self.suites:
            for rank in self.ranks:
                card = Card(rank,suite)
                self.add_to_deck(card)

    def add_to_deck(self,card):
        self.cards.append(card)

    def remove_from_deck(self,card):
        self.cards.remove(card)



    def shuffle(self):
        random.shuffle(self.cards)

    def give_cards(self, who_to, how_much_per_player):
        for rond_in_range in range(how_much_per_player):
            for who in who_to:
                if who.hit_me == True:
                    self.give_card_to(self.cards[0],who)


    def give_card_to(self,card,who):
        self.remove_from_deck(card)
        who.recive_card(card)


class Player(object):
    def __init__(self,name='John Doe'):
        self.name = name
        self.cards = []
        self.hit_me = True
        self.in_game = True
        self.iamrobot = True

    def __str__(self):
        return self.name


    def recive_card(self,card):
        self.cards.append(card)

    def return_cards_value(self):
        value = 0
        for card in self.cards:
            value += card.return_value()

        if value > 21:
            for card in self.cards:
                if card.rank == 'A' and value>21:
                    value -= 10
        return value

    def do_i_want_to_recive_card(self):
        return True


class Printer(object):

    def player_name(self,player):
        return player.name

    def player_cards(self,player):
        output = ""
        for card in player.cards:
            output += str("|{:>2} {} |  ".format(card.rank,self.change_card_suite_string_to_symbol(card)))
        return output

    def change_card_suite_string_to_symbol(self,card):
        if card.suite == 'spades':
            return '♠'
        elif card.suite == 'hearts':
            return '♥'
        elif card.suite == 'diamonds':
            return '♦'
        elif card.suite == 'clubs':
            return '♣'


    def list_players_cards_and_values(self,players):
        out = ""
        for player in players:
            out += "{:<15}".format(self.player_name(player))
            out += self.player_cards(player)
            out += "  - {}".format(player.return_cards_value())
            out += "\n"
        return out

