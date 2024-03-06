# Exercise 168. Repeating words

def repeatingWords(filename):
    file = open(filename , "r")
    words = file.read().split()
    for word1 in range(len(words)):
        for word2 in range(word1 + 1 , len(words)):
            if words[word1] == words[word2]:
                print(word2 , words[word1])

filename = input("Input filename: ")

repeatingWords(filename)