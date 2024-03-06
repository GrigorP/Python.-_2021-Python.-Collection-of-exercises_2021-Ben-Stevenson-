# Exercise 162. Books without the letter E

import string

def count_letters(filename):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    total_words = 0
    with open("Files/for_ex2.txt", 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                word = ''.join(char for char in word if char.isalnum())
                for letter in word:
                    if letter in string.ascii_lowercase:
                        letter_count[letter] += 1
                total_words += 1

    return letter_count, total_words

def main():
    filename = 'for_ex.txt'  
    letter_count, total_words = count_letters(filename)

    rarest_letter = min(letter_count, key=letter_count.get)

    print("Percentage of words containing each letter:")
    for letter in string.ascii_lowercase:
        percentage = (letter_count[letter] / total_words) * 100
        print(f"{letter.upper()}: {percentage:.2f}%")

    print(f"\nThe rarest letter found in words: {rarest_letter.upper()}")

if __name__ == "__main__":
    main()