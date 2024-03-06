# Exercise 121. Random lottery numbers

from random import sample

your_ticket = []

for _ in range(6):
    ticket_number = sample(range(1 , 49), k=1)
    your_ticket.append(ticket_number)

def lottery(your_ticket):
    for i in range(6):
        random_number = sample(range(1 , 49), k=1)
        print(random_number)
        print(your_ticket[i])
        if random_number == your_ticket[i]:
            result = True
        else:
            return False
    return result

print(lottery(your_ticket))
