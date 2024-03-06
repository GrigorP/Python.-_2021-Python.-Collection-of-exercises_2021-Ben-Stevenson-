# Exercise 112. Removing outliers

def copying_list(lst: list):
    copied_list = lst.copy()
    copied_list.remove(min(copied_list))
    copied_list.remove(max(copied_list))

    return copied_list

num = int(input("Input number(0 for close): "))
lst = []

while num:
    lst.append(num)
    num = int(input("Input number(0 for close): "))

if len(lst) < 4:
    print("You must enter more than 3 numbers.")
else:
    print(copying_list(lst))