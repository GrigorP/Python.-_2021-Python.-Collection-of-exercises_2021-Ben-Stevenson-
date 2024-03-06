# Exercise 115. List of proper divisors

def proper_divisors(number):
    divisors = []
    for i in range(1 , number):
        if number % i == 0:
            divisors.append(i)
    
    return divisors


if __name__ == "__main__":
    number = int(input("Input number: "))
    print(proper_divisors(number))