# Exercise 44. Portraits on banknotes

#dollars
George_Washington = 1   
Thomas_Jefferson = 2
Abraham_Lincoln = 5
Alexander_Hamilton = 10
Andrew_Jackson = 20
Ulysses_Grant = 50
Benjamin_Franklin = 100

banknote_denomination = int(input('Input Banknote denomination: '))

if banknote_denomination == 1:
    print('George Washington')
elif banknote_denomination == 2:
    print('Thomas Jefferson')
elif banknote_denomination == 5:
    print('Abraham Lincoln')
elif banknote_denomination == 10:
    print('Alexander Hamilton')
elif banknote_denomination == 20:
    print('Andrew Jackson')
elif banknote_denomination == 50:
    print('Ulysses Grant')
elif banknote_denomination == 100:
    print('Benjamin Franklin')
else:
    print(f'There are not partret with this ({banknote_denomination}) banknote denomination ')