# Exercise 94. Is it a triangle?

def Is_it_a_triangle(a , b , c):
    lst = [a , b ,c]
    for i in lst:
        if i <= 0:
            return False
        else:
            d = max(lst)
            lst.sort()
            if d >= lst[0] + lst[1]:
                return False
            else:
                return True
                
a = int(input("Input first side of your triangle: "))
b = int(input("Input second side of your triangle: "))
c = int(input("Input third side of your triangle: "))

print(Is_it_a_triangle(a , b , c))