# Exercise 153. Longest word in file

file_name = input("Input file name: ")
with open(file_name , "r") as file:
    words = file.read().split()
    max_word = ""
    max_words = []
    for word in words:
        if len(max_word) < len(word):
            max_word = word
            max_words = [word]
        if len(max_word) == len(word):
            if word not in max_words:
                max_words.append(word)
    print(len(max_word))
    print(max_words)
file.close()
