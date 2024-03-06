# Exercise 102. Checking password strength

def checking(password, letters: str, numbers: str):
    if len(password) >= 8:
        has_number = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)

        if has_number and has_upper and has_lower:
            return True

    return False

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = input("Input here your password: ")

def main():
    return checking(password, letters, numbers)

if __name__ == "__main__":
    print(main())