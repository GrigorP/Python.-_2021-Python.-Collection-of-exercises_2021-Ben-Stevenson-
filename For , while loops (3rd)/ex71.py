# Exercise 71. Approximate number π

count = 0
pi = 3

for i in range(2 , 30):
    if count != 15:
        if count % 2 == 0:
            pi += 4 / (i * (i + 1) * (i + 2))
        else:
            pi -= 4 / (i * (i + 1) * (i + 2))
        count += 1
        print(f"{pi}\n")


