# Exercise 59. Next day

year = int(input("Input the year: "))
month = input("Input the month (1-12): ")
day = int(input("Input the day (1-31): "))

if year % 400 == 0:
    isleapyear = True
elif year % 100 == 0:
    isleapyear = False
elif year % 4 == 0:
    isleapyear = True
else:
    isleapyear = False

list_of_months_31 = ["1" , "3" , "5" , "7" , "8" , "10" , "12"]
list_of_months_30 = ["4" , "6" , "9" , "11"]

if month in list_of_months_31:
    days = 31
elif month in list_of_months_30:
    days = 30
elif month == "2":
    if isleapyear:
        days = 29
    else:
        days = 28
else:
    print("Wrong month.")
    month = False


if month:
    month = int(month)
    if month != 12:
        if day == 31 or day == 30 or day == 29 or day == 28:
            if day == days:
                month += 1
                day = 1
                print(f"{day}.{month}.{year}")
            else:
                print("Wrong day.")
        elif day < 28:
                day += 1
                print(f"{day}.{month}.{year}")
    else:
        if day == 31:
            year += 1
            month = 1
            day = 1
            print(f"{day}.{month}.{year}")
        elif day < 31:
            day += 1
            print(f"{day}.{month}.{year}")


    
    




