# Exercise 73. Caesar Code

phrase = input("Enter the phrase to encrypt/decrypt: ")
shift = int(input("Enter the number of characters to shift: "))

result = ""

for char in phrase:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - base + shift) % 26 + base)
    else:
        result += char

print("Result:", result)