# Exercise 86. Taxi fare

def taxi_fare(km):
    m = (km * 1000) // 140 # (140m = $0.25)
    tax = 4 + (m * 0.25)
    return tax

km = int(input("Input distance(in kilometers): "))

print(f"You need to pay - ${taxi_fare(km)}")