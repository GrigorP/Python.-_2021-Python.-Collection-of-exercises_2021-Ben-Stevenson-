# Exercise 159. Random two-word password
from random import sample

def randomPassword(filename):
    file = open(filename , "r")
    words_in_file = file.read().split()
    word1 = "".join(map(str , sample(words_in_file , k=1)))
    word2 = "".join(map(str , sample(words_in_file , k=1)))
    
    while not 8 <= len(word1) + len(word2) <= 10 or not word1.isalpha() or not word2.isalpha():
        if len(word1) < 3:
            word1 = "".join(map(str , sample(words_in_file , k=1)))
        elif len(word2) < 3:
            word2 = "".join(map(str , sample(words_in_file , k=1))) 
        elif not 8 <= len(word2) + len(word1) <= 10:
            word1 = "".join(map(str , sample(words_in_file , k=1)))
            word2 = "".join(map(str , sample(words_in_file , k=1)))
        else:
            if not word1.isalpha():
                word1 = "".join(map(str , sample(words_in_file , k=1)))
            if not word2.isalpha():
                word2 = "".join(map(str , sample(words_in_file , k=1)))
    password = word1.capitalize() + word2.capitalize() 

    return password

filename = input("Input filename: ")

print(randomPassword(filename))
    