# Exercise 167. Checking the spelling

import sys
import string

def load_dictionary(dictionary_file):
    dictionary = set()
    with open(dictionary_file, 'r') as file:
        for word in file:
            dictionary.add(word.strip().lower())
    return dictionary

def spell_check(text_file, dictionary):
    misspelled_words = []
    with open(text_file, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.strip(string.punctuation).lower()
                if word not in dictionary:
                    misspelled_words.append(word)
    return misspelled_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python spell_checker.py <text_file>")
        sys.exit(1)
    text_file = sys.argv[1]

    dictionary_file = "for_ex.txt"  
    dictionary = load_dictionary(dictionary_file)

    misspelled_words = spell_check(text_file, dictionary)

    if misspelled_words:
        print("Misspelled words:")
        for word in misspelled_words:
            print(word)
    else:
        print("No misspelled words found.")

if __name__ == "__main__":
    main()