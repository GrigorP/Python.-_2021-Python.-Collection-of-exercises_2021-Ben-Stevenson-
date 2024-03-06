# Exercise 84. Tossing a coin
from random import choice
# appear = O
# heads = P
values = ["O" , "P"]
count = 0
for _ in range(1, 11):
    dropped_out_values = []
    while len(dropped_out_values) != 3:
        dropped_out_values.append(choice(values))
    new = dropped_out_values[-4:]   
    while new[-1] != new[-2] or new[-1] != new[-3]:
        dropped_out_values.append(choice(values))
        new = dropped_out_values[-3:]  
    print(dropped_out_values)
    print(f"Attempts - {len(dropped_out_values)}")
    count += len(dropped_out_values)

print(f"Average number of attempts - {count / 10}")