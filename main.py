import random

CARD_COLORS = ["s", "h", "d", "c"]

class Card:
    def __init__(self,card_value, card_color):
        self.card_value = card_value
        self.card_color = card_color
    def __str__(self):
        return f'{self.card_value}{self.card_color}'

class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(2, 15):
            for color in CARD_COLORS:
                self.cards.append(Card(str(rank), color))
        random.shuffle(self.cards)

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def __str__(self):
        return f'{self.name}'

class Table:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck


deck = Deck()

player_1, player_2 = [Player(f'player{i}', []) for i in range(1, 3)]

table = (Table([player_1, player_2], deck))

for i in range(2):
    player_1.hand.append(table.deck.cards.pop())
    player_2.hand.append(table.deck.cards.pop())
  
hand_1 = 'PLAYER 1 : '
for card in player_1.hand:
    hand_1 += str(card) + ' '
print(hand_1 + '\n')

hand_2 = 'PLAYER 2 : '
for card in player_2.hand:
    hand_2 += str(card) + ' '
print(hand_2)

river = [table.deck.cards.pop() for x in range(5)]
river_string = '\n************** '
for card in river:
    river_string += str(card) + ' '
print(str.rstrip(river_string) + ' **************')

def compare_hands(hand1, hand2, river):
    result1 = ''
    result2 = ''
    comparaison_1 = [*hand1, *river]
    comparaison_2 = [*hand2, *river]
    for card in comparaison_1:
        result1 += str(card) + ' '
    for card in comparaison_2:
        result2 += str(card) + ' '
    return '\nPLAYER 1 : ' + result1 + '\n\nPLAYER 2 : ' + result2 + '\n'


print(compare_hands(player_1.hand, player_2.hand, river))
