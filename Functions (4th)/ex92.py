# Exercise 92. Ordinal date in Gregorian calendar

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def ordinal_to_date(ordinal_date):
    year = 1
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if ordinal_date <= days_in_year:
            break
        ordinal_date -= days_in_year
        year += 1

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    month = 1
    while ordinal_date > days_in_month[month]:
        ordinal_date -= days_in_month[month]
        month += 1

    return ordinal_date, month, year

def main():
    ordinal_date = int(input("Enter the ordinal date (e.g., 1st January is 1): "))
    result = ordinal_to_date(ordinal_date)

    if isinstance(result, tuple):
        day, month, year = result
        print(f"Corresponding date: {day}/{month}/{year}")
    else:
        print(result)

if __name__ == "__main__":
    main()