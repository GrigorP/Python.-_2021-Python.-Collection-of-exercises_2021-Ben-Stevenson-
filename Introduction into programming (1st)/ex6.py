# Exercise 6. Taxes and tips

TAX = 0.50
sums = float(input('Input sum: '))
sums_officiant = (sums * 18) / 100

print(f'$ {sums + TAX + sums_officiant:.2f}')