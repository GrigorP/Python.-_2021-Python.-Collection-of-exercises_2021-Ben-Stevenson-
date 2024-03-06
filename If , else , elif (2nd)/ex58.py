# Упражнение 58. Високосный год?

year = int(input("Inout year: "))

if year % 400 == 0:
    isleapyear = True
elif year % 100 == 0:
    isleapyear = False
elif year % 4 == 0:
    isleapyear = True
else:
    isleapyear = False

print(isleapyear)