# Exercise 50. Richter scale

magnitude = int(input('Input earthquake magnitude: '))

if magnitude < 2:
    print('Minimum')
elif 2 <= magnitude < 3:
    print('Very weak')
elif 3 <= magnitude < 4:
    print('Weak')
elif 4 <= magnitude < 5:
    print('Intermediate')
elif 5 <= magnitude < 6:
    print('Moderate')
elif 6 <= magnitude < 7:
    print('Strong')
elif 7 <= magnitude < 8:
    print('Very strong')
elif 8 <= magnitude < 10:
    print('Huge')
else:
    print('Destructive')
