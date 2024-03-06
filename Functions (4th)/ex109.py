# Exercise 109. Magic dates

def magic_dates(day , month , year: str):
    result = 0
    if len(year) >= 4:
        year = int(year[-2:])
    else:
        result =  "Enter the year in the 20th+ century."
        return result
    if 1 <= month <= 12:    
        if 1 <= day <= 31:
            if day * month == year:
                result = "True"
            else:
                result = "False"
        else:
            result = "Wrong day."
    else:
        result = "Wrong month."
    
    return result

day = int(input("Input day: "))
month = int(input("Input month: "))
year = input("Input year: ")

print(magic_dates(day , month , year))