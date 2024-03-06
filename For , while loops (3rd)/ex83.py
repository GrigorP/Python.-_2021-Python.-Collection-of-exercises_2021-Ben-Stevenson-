# Exercise 83. Maximum number in sequence

from random import sample

changed_elements = []

a = sample(range(1 , 101) , k=1)
a = int(a[0])

max_element = a
print(max_element)
while max_element != 100:
    a = sample(range(1 , 101) , k=1)
    a = int(a[0])

    if a > max_element:
        print(a, ">", max_element)
        max_element = a
        changed_elements += [a]
    print(a)

print(changed_elements)
print(f"Number of maximum value changes - {len(changed_elements)}")