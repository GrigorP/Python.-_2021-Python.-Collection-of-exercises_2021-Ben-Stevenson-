# Exercise 179. Recursive square root

def recSquareRoot(n , guess):
    if abs(guess * guess - n) < 1e-12:
        return guess
    else:
        return recSquareRoot(n , guess = 0.5 * (guess + n / guess))
    
    
n = int(input("Input number: "))
print(f"{recSquareRoot(n , 1):.1f}")