#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

""" spades (♠), hearts (♥), diamonds (♦) and clubs (♣)"""


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
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.hit_me = True
        self.in_game = True

    def recive_card(self,card):
        self.cards.append(card)

