# Exercise 91. Gregorian calendar in ordinal

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def ordinalDate(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    if month < 1 or month > 12 or day < 1 or day > days_in_month[month]:
        return "Invalid date"

    ordinal_day = sum(days_in_month[:month]) + day
    return ordinal_day

def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    result = ordinalDate(day, month, year)

    if isinstance(result, str):
        print(result)
    else:
        print(f"Ordinal day number: {result}")

if __name__ == "__main__":
    main()