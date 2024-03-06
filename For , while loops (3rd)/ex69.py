# Exercise 69. Tickets to the zoo

age = int(input("Input person age(blank for close): "))
pay_for_ticket = 0

while age:
    age = int(age)
    if age <= 2:
        pay_for_ticket += 0
    elif 2 < age <= 12:
        pay_for_ticket += 14.00
    elif age > 65:
        pay_for_ticket += 18.00
    else:
        pay_for_ticket += 23.00
    age = input("Input person age(blank for close): ")

print(f"For zoo You need to pay - ${pay_for_ticket:.2f}")