# Exercise 173. Sum of values

def sumValues():
    num = input("Enter a number (press Enter to finish): ")
    if num == "":
        return 0.0
    else:
        try:
            return float(num) + sumValues()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return sumValues()

print(sumValues())