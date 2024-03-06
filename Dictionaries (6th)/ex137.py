# Exercise 137. Two dice

import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_throws(num_throws):
    results = {}
    for _ in range(num_throws):
        total = roll_dice()
        results[total] = results.get(total, 0) + 1
    return results

def display_summary(results):
    print("Outcome\tSimulation percentage\tExpected percentage")
    for outcome in range(2, 13):
        simulation_percent = (results.get(outcome, 0) / num_throws) * 100
        expected_percent = (1/36) * 100
        print(f"{outcome}\t{simulation_percent:.2f}\t{expected_percent:.2f}")

if __name__ == "__main__":
    num_throws = 1000
    results = simulate_throws(num_throws)
    display_summary(results)