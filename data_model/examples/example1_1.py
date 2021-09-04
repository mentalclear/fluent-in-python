import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] 

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])
print("\n")

for i in range(1, 4):
    print(choice(deck))

print("\nSlicing:")
# Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing.
print(deck[:3])

print(deck[12::13])

# Just by implementing the __getitem__ special method, our deck is also iterable:
print("\nIterating:")
for card in deck:
    print(card)

print("\nIterating in reverse:")
for card in reversed(deck):
    print(card)


# checking the deck for a specific car laso works
print("\nChecking the card:")
print(Card('Q', 'diamonds') in deck)
print(Card('Q', 'something') in deck)

# A common system of ranking cards is by rank (with aces being highest), 
# then by suit in the order of spades (highest), 
# hearts, diamonds, and clubs (lowest). Here is a function that ranks cards by that rule, 
# returning 0 for the 2 of clubs and 51 for the ace of spades:

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Given spades_high, we can now list our deck in order of increasing rank:
print("\ncards in order:")
for card in sorted(deck, key=spades_high):
    print(card)