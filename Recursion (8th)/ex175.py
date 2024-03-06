# Exercise 175. Recursive translation of a number decimal to binary

def decToBinRec(num):
    if num <= 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return str(num % 2) + decToBinRec(num // 2)
    

num = int(input("Input number: "))
print(decToBinRec(num)[::-1])
    

    