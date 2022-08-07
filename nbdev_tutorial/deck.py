# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../01_deck.ipynb 3
from .card import *
from fastcore.basics import *
from fastcore.test import *
import random

# %% ../01_deck.ipynb 4
class Deck:
    "Represents a deck of cards"
    def __init__(self): self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
    def __str__(self): return '; '.join(map(str, self.cards))
    def __len__(self): return len(self.cards)
    def __contains__(self, card): return card in self.cards
    __repr__ = __str__
    
    def add(self,
            card:Card): # Card to add
        "Adds `card` to the deck"
        self.cards.append(card)

    def remove(self,
               card:Card): # Card to remove
        "Removes `card` from the deck or raises exception if it is not there"
        self.cards.remove(card)

    def shuffle(self):
        "Shuffles the cards in this deck"
        random.shuffle(self.cards)
