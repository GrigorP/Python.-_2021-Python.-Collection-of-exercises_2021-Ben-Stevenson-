# Exercise 126. Dealing pocket cards

from random import choice

def createDeck():
    par_cards = ["2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" , "A"]
    card_suit = ["s" , "h" , "d" , "c"]
    deck =  [i + j for i in par_cards for j in card_suit]
    return deck

deck = createDeck()

def shuffle(deck: list):
    for _ in range(52):
        num = choice(range(51))
        elem = deck.pop(num)
        element = deck[num]
        deck[num] = elem
        deck.append(element)
    return deck

shuffled_deck = shuffle(deck)

def deal(number_of_players: int , quantity_of_cards_for_player: int , deck: list):
    players = []
    for i in range(number_of_players):
        player_cards = [deck.pop() for _ in range(quantity_of_cards_for_player)]
        players.append(player_cards)
    print(deck)
    return players

players = deal( 4 , 5 , shuffled_deck)

for i, player_cards in enumerate(players):
    print(f"Player {i+1} cards:", player_cards)