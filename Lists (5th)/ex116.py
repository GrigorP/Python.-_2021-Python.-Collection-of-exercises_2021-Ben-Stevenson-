# Exercise 116. Perfect numbers

def proper_divisors(number):
    divisors = []
    result = False
    for i in range(1 , number):
        if number % i == 0:
            divisors.append(i)
            
    if sum(divisors) == number:
        result = True
    else:
        result = False
    
    return result

number = int(input("Input number: "))
print(proper_divisors(number))