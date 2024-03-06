# Exercise 39. How many days are there in a month?

month = input('Input month: ')

months_31 = ['january' , 'march' , 'may' , 'july' , 'august' , 'october' , 'december']
months_30 = ['april' , 'june' , 'september' , 'november']

if month.lower() in  months_31:
    print(f'In {month} are 31 days. ')
elif month.lower() in months_30:
    print(f'In {month} are 30 days. ')
elif month.lower() == 'february':
    print('February can be 28 or 29 days.')
else:
    print(f'There are no month named - {month}')