# Exercise 46. What color is the cell?(Chess)

letter = input('Input letter(a-h): ')
number = int(input('Input number(1-8): '))

if 1 <= number <= 8:
    if letter in 'aceg':
        if number % 2 == 0:
            print('White')
        else:
            print('Black')
    elif letter in 'bdfh':
        if number % 2 == 0:
            print('Black')
        else:
            print('White')
    else:
        print('Wrong coordinades.')
else:
    print('Wrong coordinades.')