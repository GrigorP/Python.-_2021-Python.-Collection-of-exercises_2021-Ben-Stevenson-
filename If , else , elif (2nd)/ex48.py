# Exercise 48. Zodiac signs

day_of_date = int(input('Input here day of the date: '))
month_of_date = input('Input here month of the date: ')

if 1 <= day_of_date <= 31:
    if month_of_date.lower() == 'january':
        if day_of_date <= 19:
            print('Capricorn.')
        else:
            print('Aquarius.')
    elif month_of_date.lower() == 'february':
        if day_of_date <= 18:
            print('Aquarius.')
        else:
            print('Fish.')
    elif month_of_date.lower() == 'march':
        if day_of_date <= 20:
            print('Fish.')
        else:
            print('Aries.')
    elif month_of_date.lower() == 'april':
        if day_of_date <= 19:
            print('Aries.')
        else:
            print('Taurus.')
    elif month_of_date.lower() == 'may':
        if day_of_date <= 20:
            print('Taurus.')
        else:
            print('Twins.')
    elif month_of_date.lower() == 'june':
        if day_of_date <= 20:
            print('Twins.')
        else:
            print('Cancer.')
    elif month_of_date.lower() == 'july':
        if day_of_date <= 22:
            print('Cancer.')
        else:
            print('Leo.')
    elif month_of_date.lower() == 'august':
        if day_of_date <= 22:
            print('Leo.')
        else:
            print('Virgo.')
    elif month_of_date.lower() == 'september':
        if day_of_date <= 22:
            print('Virgo.')
        else:
            print('Scales.')
    elif month_of_date.lower() == 'october':
        if day_of_date <= 22:
            print('Scales.')
        else:
            print('Scorpion.')
    elif month_of_date.lower() == 'november':
        if day_of_date <= 21:
            print('Scorpion')
        else:
            print('Sagittarius.')
    elif month_of_date.lower() == 'december':
        if day_of_date <= 21:
            print('Sagittarius.')
        else:
            print('Capricorn.')
    else:
        print('Wrong month.')
else:
    print('Wrong day.')