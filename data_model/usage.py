from data_model.card_deck import Card, FrenchDeck
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
