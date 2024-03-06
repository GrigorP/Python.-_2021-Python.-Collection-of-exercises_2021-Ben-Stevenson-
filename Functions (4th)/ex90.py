# Exercise 90. The Twelve Days of Christmas

def generate_gift(day):
    gifts = [
        "A partridge in a pear tree",
        "Two turtle doves",
        "Three French hens",
        "Four calling birds",
        "Five golden rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
    ]

    verse = f"On the {ordinal(day)} day of Christmas\nmy true love sent to me:"
    
    for i in range(day, 0, -1):
        if i == 1 and day > 1:
            verse += "\nAnd " + gifts[i-1] + ","
        else:
            verse += "\n" + gifts[i-1] + ","

    return verse

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    
    return f"{n}{suffix}"

def main():
    for day in range(1, 13):
        print(generate_gift(day))
        print()

if __name__ == "__main__":
    main()