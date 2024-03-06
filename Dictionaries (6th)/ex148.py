# Exercise 148. Playing lotto

from random import shuffle
from ex146 import lotoCard

def simulate_lotto():
    winning_card = lotoCard()
    numbers = list(range(1, 76))
    shuffle(numbers)

    draws = 0
    while True:
        draws += 1
        drawn_number = numbers.pop()
        for row in winning_card.values():
            if drawn_number in row:
                row[row.index(drawn_number)] = 0

        if all(all(num == 0 for num in row) for row in winning_card.values()):
            break

    return draws

def main():
    num_simulations = 1000
    draws_needed = []

    for _ in range(num_simulations):
        draws_needed.append(simulate_lotto())

    min_draws = min(draws_needed)
    max_draws = max(draws_needed)
    avg_draws = sum(draws_needed) / num_simulations

    print(f"Minimum draws required: {min_draws}")
    print(f"Maximum draws required: {max_draws}")
    print(f"Average draws required: {avg_draws}")

if __name__ == "__main__":
    main()