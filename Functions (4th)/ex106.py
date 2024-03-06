# Exercise 106. Days in a month

def days_in_month(year , month):
    result = 0
    list_of_months_31 = [1 , 3 , 5 , 7 , 8 , 10 , 12]
    list_of_months_30 = [4 , 6 , 9 , 11]
    if year % 400 == 0:
        isleapyear = True
    elif year % 100 == 0:
        isleapyear = False
    elif year % 4 == 0:
        isleapyear = True
    else:
        isleapyear = False
    if 1 <= month <= 12:
        if isleapyear:
            if month in list_of_months_30:
                result = 30
            elif month in list_of_months_31:
                result = 31
            else:
                result = 29
        else:
            if month in list_of_months_30:
                result = 30
            elif month in list_of_months_31:
                result = 31
            else:
                result = 28
    else:
        result = "Wrong month."
    
    return result
    
year = int(input("Input year: "))
month = int(input("Input month: "))

print(days_in_month(year , month))