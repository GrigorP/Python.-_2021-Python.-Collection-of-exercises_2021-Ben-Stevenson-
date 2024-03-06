# Exercise 64. Table with discounts

discount_prices = [4.95 , 9.95 , 14.95 , 19.95 , 24.95]
old_prices = []

for price in discount_prices:
    old_prices += [round((price * 100 / 60) , 2)]

print(f"Discount prices - {discount_prices}.")
print(f"Old prices - {old_prices}.")