from random import shuffle
from itertools import product 

Suits = ["\u2663", "\u2665", "\u2666", "\u2660"] 
Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
Deck = []

def makeDeck():
    unDeck = list(product(Ranks, Suits)) 
    for i in range(0, len(unDeck)):
        Deck.append(unDeck[i][0] + unDeck[i][1])
    shuffle(Deck)


# To Print the Deck:
#     for i in DeckBuild.Deck:
#       print(i, end=" ")