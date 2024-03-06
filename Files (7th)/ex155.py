# Exercise 155. Frequency of words in a file

file_name = input("Input file name: ")
with open(file_name) as file:
    words_file = file.read().split()
    words = []
    for word in words_file:
        if word.isalnum():
            if word not in words:
                words.append(word)

for word in words:
    print(word , "-" , words_file.count(word))
file.close()