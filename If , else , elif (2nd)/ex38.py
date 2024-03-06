# Exercise 38. Guess the figure

sides = int(input('Input quantity sides of your figure: '))

if 2 < sides <= 10:
    if sides == 3:
        print('Your figure is a Triangle. ')
    if sides == 4:
        print('Your figur is a Quadrilateral. ')
    if sides == 5:
        print('Your figur is a Pentagon. ')
    if sides == 6:
        print('Your figur is a Hexagon. ')
    if sides == 7:
        print('Your figur is a Septagon. ')
    if sides == 8:
        print('Your figur is a Octagon. ')
    if sides == 9:
        print('Your figur is a Nanogon. ')
    if sides == 10:
        print('Your figur is a Decagon. ')
else:
    print('The sides yould be > 2 and < 11')