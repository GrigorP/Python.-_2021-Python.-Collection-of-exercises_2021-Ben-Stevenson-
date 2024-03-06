# Exercise 125. Shuffling a deck of cards

from random import choice

def createDeck():
    par_cards = ["2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" , "A"]
    card_suit = ["s" , "h" , "d" , "c"]
    deck =  [i + j for i in par_cards for j in card_suit]
    return deck

deck = createDeck()
print(deck)

def shuffle(deck: list):
    for _ in range(52):
        num = choice(range(51))
        elem = deck.pop(num)
        element = deck[num]
        deck[num] = elem
        deck.append(element)
    return deck

if __name__ == "__main__":
    print(shuffle(deck))