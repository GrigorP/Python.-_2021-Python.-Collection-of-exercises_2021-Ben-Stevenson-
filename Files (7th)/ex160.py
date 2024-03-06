# Exercise 160. Strange words

import random

def strangeWords(filename , word):
    file = open(filename , "a")
    if "ei" in word:
        if word.lower() == "weird":
            file.write(word)
        else:
            if "cei" in word:
                file.write(word)
            else:
                print("The word is spelled incorrectly.")
    elif "ie" in word:
        if word.lower() != "wierd":
            if "cie" not in word:
                    file.write(word)
            else:
                print("The word is spelled incorrectly.")
        else:
                print("The word is spelled incorrectly.")

filename = input("Input filename: ")
word = input("Input word: ")
strangeWords(filename , word)





