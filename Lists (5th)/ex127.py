# Exercise 127: Is the list already sorted?

def alreadySorted(lst: list):
    return True if lst == sorted(lst) else False
    
num = input("Input number: ")
lst = []

while num:
    lst.append(int(num))
    num = input("Input number (blank for close): ")

print(alreadySorted(lst))