# Exercise 49. Chinese horoscope

year = int(input('Input here a year: '))

if year <= 1999:
    if (2000 - year) % 12 == 0:
        print('Dragon')
    elif (2001 - year) % 12 == 0:
        print('Snake')
    elif (2002 - year) % 12 == 0:
        print('Horse')
    elif (2003 - year) % 12 == 0:
        print('Goat')
    elif (2004 - year) % 12 == 0:
        print('Monkey')
    elif (2005 - year) % 12 == 0:
        print('Rooster')
    elif (2006 - year) % 12 == 0:
        print('Dog')
    elif (2007 - year) % 12 == 0:
        print('Pig')
    elif (2008 - year) % 12 == 0:
        print('Rat')
    elif (2009 - year) % 12 == 0:
        print('Bull')
    elif (2010 - year) % 12 == 0:
        print('Tiger')
    elif (2011 - year) % 12 == 0:
        print('Rabbit')
else:
    if (year - 2000) % 12 == 0:
        print('Dragon')
    elif (year - 2001) % 12 == 0:
        print('Snake')
    elif (year - 2002) % 12 == 0:
        print('Horse')
    elif (year - 2003) % 12 == 0:
        print('Goat')
    elif (year - 2004) % 12 == 0:
        print('Monkey')
    elif (year - 2005) % 12 == 0:
        print('Rooster')
    elif (year - 2006) % 12 == 0:
        print('Dog')
    elif (year - 2007) % 12 == 0:
        print('Pig')
    elif (year - 2008) % 12 == 0:
        print('Rat')
    elif (year - 2009) % 12 == 0:
        print('Bull')
    elif (year - 2010) % 12 == 0:
        print('Tiger')
    elif (year - 2011) % 12 == 0:
        print('Rabbit')
