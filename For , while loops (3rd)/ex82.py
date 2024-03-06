# Exercise 82. Decimal to binary

q = int(input("Input number(decimal): "))

result = ""

while q != 0:
    r = q % 2
    result += str(r)
    q = q // 2


print(result[::-1])