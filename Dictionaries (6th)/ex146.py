# Exercise 146. Lotto card

from random import sample

def lotoCard():
    START = 1
    END = 15
    card = dict()
    for i in "BINGO":
        card[i] = sample(range(START , END) , k=5)
        END += 15
        START += 15

    return card

def displayCard(lotto_card): 
    print(" B   I   N   G   O")
    for i in range(5):
        print('{:2} {:3} {:3} {:3} {:3}'.format(lotto_card['B'][i], lotto_card['I'][i], lotto_card['N'][i], lotto_card['G'][i], lotto_card['O'][i]))


if __name__ == "__main__":
    card = lotoCard()
    displayCard(card)