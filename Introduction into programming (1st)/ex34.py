# Exercise 34. Yesterday's bread

bread = 3.49 

quantity_of_breads = int(input('Input quantity of yesterday`s bread: '))

print(f'The Price of bread - {bread}')
print(f'The Dicount price of bread - {bread * 60 // 100}')
print(f'The Price you need to pay - {quantity_of_breads * (bread * 60 // 100)}')