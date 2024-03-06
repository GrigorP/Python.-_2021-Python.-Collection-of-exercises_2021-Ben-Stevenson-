# Exercise 87. Calculating shipping costs

def shipping_costs(quantity):
    result = 10.95 # 10.95 for first product
    if quantity > 1:
        result += (quantity - 1) * 2.95
        return result
    else:
        return result

quantity = int(input("Input here a quantity of your products: "))

print(f"You need to pay - {shipping_costs(quantity)}")