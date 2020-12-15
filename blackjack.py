SUITS = ["♥️", "♠️", "♣️", "♦️"]
RANKS = ["Ace", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10]



class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'card is a {self.rank} of {self.suit}'

class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

my_deck = Deck(SUITS, RANKS)
for card in my_deck.cards:
    print(card)

