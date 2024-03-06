# Exercise 25. Time units (second)

sec = int(input("Input seconds: "))

days = sec // 86400
sec -= 86400 * days

hours = sec // 3600
sec -= 3600 * hours

minutes = sec // 60
sec -= 60 * minutes

print(f'D - {days} : HH - {hours} : MM - {minutes} : SS - {sec}')