# Exercise 47. Determining the time of year

month = input('Input Month: ')

winter = ['december' , 'january' , 'february']
autumn = ['september' , 'october', 'november']
summer = ['june' , 'july' , 'august']
spring = ['march' , 'april', 'may']

if month.lower() in winter:
    print('Winter.')
elif month.lower() in autumn:
    print('Autumn.')
elif month.lower() in summer:
    print('Summer.')
elif month.lower() in spring:
    print('Spring.')
else:
    print('Wrong month.')