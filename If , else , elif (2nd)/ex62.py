# Exercise 62. Playing roulette

from random import choice as c

red = ["1" , "3" , "5" , "7" , "9" , "12" , "14" , "16" , "18" , "19" , "21" , "23" , "25" , "27" , "30" , "32" , "34" , "36"]
black = ["2" , "4" , "6" , "8" , "10" ,"11" ,"13" , "15" , "17" , "20" , "22" , "24" , "26" , "28" , "29" , "31" , "33" , "35"]
green = ["0" , "00"]

choice = int(input("Input how you want to place your bet: \
\n1 - numbers(1-36 , 0 or 00)\
\n2 - red or black\
\n3 - even or odd(witout 0 and 00)\
\n-> "))

if choice == 1:
    num = int(input("Input number (1-36 , 0 or 00): "))
    color = False
    parity = False
elif choice == 2:
    color = input("Input here color (red or black): ")
    num = False
    parity = False
elif choice == 3:
    parity = input("Input parity (even or odd): ")
    num = False
    color = False
else:
    print("Wrong choice.")


all_numbers = list(red + black + green)

winnig_number = c(all_numbers)
winnig_number = int(winnig_number)

if choice <= 3:
    if 1 <= winnig_number <= 18:
        if winnig_number % 2 == 0:
            winnig_number = str(winnig_number)
            if winnig_number in red:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Red")
                print("Even")
                print("1 - 18")
                print("----------------------------")
            elif winnig_number in black:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Black")
                print("Even")
                print("1 - 18")
                print("----------------------------")
        else:
            winnig_number = str(winnig_number)
            if winnig_number in red:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Red")
                print("Odd")
                print("1 - 18")
                print("----------------------------")
            elif winnig_number in black:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Black")
                print("Odd")
                print("1 - 18")
                print("----------------------------")
    elif 19 <= winnig_number <= 36:
        if winnig_number % 2 == 0:
            winnig_number = str(winnig_number)
            if winnig_number in red:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Red")
                print("Even")
                print("19 - 36")
                print("----------------------------")
            elif winnig_number in black:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Black")
                print("Even")
                print("19 - 36")
                print("----------------------------")
        else:
            winnig_number = str(winnig_number)
            if winnig_number in red:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Red")
                print("Odd")
                print("1 - 18")
                print("----------------------------")
            elif winnig_number in black:
                print(f"Winning number - {winnig_number}.")
                print(f"Winning bet - {winnig_number}.")
                print("Black")
                print("Odd")
                print("1 - 18")
                print("----------------------------")
    elif winnig_number == 0 or winnig_number == 00:
        print(f"Winning number - {winnig_number}.")
        print(f"Winning bet - {winnig_number}.")

if choice <= 3:
    if num:
        if num <= 36:
            if num == winnig_number:
                print("You Win!")
            else:
                print("You didn't win!")
        else:
            print("Wrong number!")
    elif color:
        if color.lower() == "red":
            if winnig_number in red:
                print("You Win!")
            elif winnig_number in black:
                print("You didn't win!")
            elif winnig_number in green:
                print("You didn't win!")
        elif color.lower() ==  "black":
            if winnig_number in red:
                print("You didn't win!")
            elif winnig_number in black:
                print("You Win!")
            elif winnig_number in green:
                print("You didn't win!")
        else:
            print("Wrong color.")
    elif parity:
        if parity.lower() == "even":
            winnig_number = int(winnig_number)
            if winnig_number % 2 == 0:
                print("You Win!")
            else:
                print("You didn't win!")
        elif parity.lower() == "odd":
            winnig_number = int(winnig_number)
            if winnig_number % 2 == 0:
                print("You didn't win!")
            else:
                print("You Win!")
        else:
            print("Wrong parity:")
