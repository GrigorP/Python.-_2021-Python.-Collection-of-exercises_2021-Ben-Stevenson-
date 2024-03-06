# Exercise 24. Time units (first)

days = int(input('Input days: '))
hours = int(input('Input hours: '))
minutes = int(input('Input minutes: '))
seconds = int(input('Input seconds: '))

time = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

print(f'The time in seconds -> {time}')