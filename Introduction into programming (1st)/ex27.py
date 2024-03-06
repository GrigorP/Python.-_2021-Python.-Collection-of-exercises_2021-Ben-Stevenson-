# Exercise 27. When is Easter?

year = int(input('The year which you interested in the date of Easter: '))

a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = ((19 * a) + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + (2 * e) + (2 * i) - h - k) % 7
m = (a + (11 * h) + (22 * i)) // 451
month = (h + l + (7 * m) + 114) // 31
day = 1 + ((h + l - (7 * m) + 114) % 31)
print(f'This is a month of Easter - {month}')
print(f'This is a day of Easter - {day}')