from data_model.card_deck import Card, FrenchDeck, spades_high
from data_model.vector import Vector
from random import choice

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

for card in sorted(deck, key=spades_high):
    print(card)


# Although FrenchDeck implicitly inherits from object[6], its functionality is not inherited, 
# but comes from leveraging the Data Model and composition.
# By implementing the special methods __len__ and __getitem__ our FrenchDeck behaves like a standard Python sequence,
# allowing it to benefit from core language features—like iteration and slicing—and from the standard library,
# as shown by the examples using random.choice, reversed and sorted.
# Thanks to composition, the __len__ and __getitem__ implementations can hand off all the work to a list object, self._cards.

v1 = Vector(1, 2)
v2 = Vector(3, 5)
v3 = v1 + v2
print(v3)

v = Vector(4, 5)
print(abs(v))

print(v * 3)