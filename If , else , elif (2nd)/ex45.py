# Exercise 45. Holiday dates

day = int(input('Input here day for holiday: '))
month = input('Input here month for oliday: ')

if day == 1 and month.lower() == 'january':
    print('The holiday is New Year.')
elif day == 1 and month.lower() == 'july':
    print('The holiday is Canada Day.')
elif day == 25 and month.lower() == 'december':
    print('The holiday is Christmas.')
else:
    print(f'In Canada no holiday in day - {day} and month - {month}')