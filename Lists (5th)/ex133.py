# Exercise 133: Does a list contain a subset of elements?

def isSublist(larger, smaller):
    if len(smaller) == 0:
        return True
    
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:
            return True
    
    return False

num = input("Input numbers for larger list: ")
larger = []

while num:
    larger.append(int(num))
    num = input("Input numbers for larger list: ")

num = input("Input numbers for smaller list: ")
smaller = []

while num:
    smaller.append(int(num))
    num = input("Input numbers for smaller list: ")

print(isSublist(larger , smaller))