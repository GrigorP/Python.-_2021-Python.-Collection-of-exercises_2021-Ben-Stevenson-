# Exercise 88. Median of three values

def median(a , b , c):
    result = (a + b + c) / 3
    return result

a = int(input("Input here first value: "))
b = int(input("Input here second value: "))
c = int(input("Input here third value: "))

print(f"The median of your values - {median(a,b,c)}")