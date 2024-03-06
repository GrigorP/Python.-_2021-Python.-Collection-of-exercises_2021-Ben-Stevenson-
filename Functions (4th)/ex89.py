# Exercise 89. Converting integers to numerals

def main(number):
    if 1 <= number <= 12:
        if number == 1:
            return "First"
        elif number == 2:
            return "Second"
        elif number == 3:
            return "Third"
        elif number == 4:
            return "Fourth"
        elif number == 5:
            return "Fifth"
        elif number == 6:
            return "Sixth"
        elif number == 7:
            return "Seventh"
        elif number == 8:
            return "Eighth"
        elif number == 9:
            return "Ninth"
        elif number == 10:
            return "Tenth"
        elif number == 11:
            return "Eleventh"
        else:
            return "Twelfth"
    else:
        return "Your number must be > 0 and < 13"
    
number = int(input("Input here your number: "))

if __name__ == "__main__":
    print(main(number))
