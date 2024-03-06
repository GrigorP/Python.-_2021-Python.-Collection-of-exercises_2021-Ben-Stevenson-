# Exercise 77. Multiplication table

for i in range(1, 11):
    print(f"{i:2}", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
    