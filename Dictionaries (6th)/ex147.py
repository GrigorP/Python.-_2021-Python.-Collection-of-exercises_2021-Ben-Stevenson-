# Exercise 147. Checking the card

from random import randrange
from ex146 import lotoCard

def displayCards(lotto_cards): 
    print(" B   I   N   G   O" , end="     ")
    print(" B   I   N   G   O" , end="     ")
    print(" B   I   N   G   O")
    for row in range(5):
        for card in lotto_cards:
            print('{:2} {:3} {:3} {:3} {:3}'.format(card['B'][row], card['I'][row], card['N'][row], card['G'][row], card['O'][row]), end="     ")
        print()


def nullification(card1: dict , card2: dict , card3: dict):
    cards = [card1 , card2 , card3]
    num = randrange(1 , 76)
    for i in cards:
        for values in i.values():
            for value in values:
                if value == num:
                    values[values.index(value)] = 0
    return cards

def is_win_row(card1: dict , card2: dict , card3: dict):
    cards = [card1 , card2 , card3]
    for card in cards:
        for i in range(len(card)):
            sum_row = 0
            for value in card.values():
                sum_row += value[i]
            if sum_row == 0:
                return True
    return False

def is_win_col(card1: dict , card2: dict , card3: dict):
    cards = [card1 , card2 , card3]
    for card in cards:
        for value in card.values():
            if sum(value) == 0:
                return True
    return False

def is_win_diag(card1: dict , card2: dict , card3: dict):
    cards = [card1 , card2 , card3]
    sum_diag = 0
    for card in cards:
        for value in card.values():
            for i in range(5):
                sum_diag += value[i]
            if sum_diag == 0:
                return True
    sum_diag = 0
    for card in cards:
        for value in card.values():
            for i in range(1 , 6):
                sum_diag += value[-i]
            if sum_diag == 0:
                return True
    return False

def playing_loto_with_3_cards(card1: dict , card2: dict , card3: dict):
    cards = [card1 , card2 , card3]
    while True:
        nullification(card1 , card2 , card3)
        if is_win_col(card1 , card2 , card3):
            break
        if is_win_row(card1 , card2 , card3):
            break
        if is_win_diag(card1 , card2 , card3):
            break
    displayCards(cards)

if __name__ == "__main__":
    card1 = lotoCard()
    card2 = lotoCard()
    card3 = lotoCard()

    playing_loto_with_3_cards(card1 , card2 , card3)