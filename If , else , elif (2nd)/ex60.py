# Exercise 60. What day of the week does January 1st fall on?

from math import floor

year = int(input("Input the year: "))

day_of_the_week = (year + floor((year - 1)/4) - floor((year - 1)/100) + floor((year - 1)/400))%7

if day_of_the_week == 0:
    print("Sunday.")
elif day_of_the_week == 1:
    print("Monday.")
elif day_of_the_week == 2:
    print("Tuesday.")
elif day_of_the_week == 3:
    print("Wednesday.")
elif day_of_the_week == 4:
    print("Thursday.")
elif day_of_the_week == 5:
    print("Friday.")
elif day_of_the_week == 6:
    print("Saturday.")
