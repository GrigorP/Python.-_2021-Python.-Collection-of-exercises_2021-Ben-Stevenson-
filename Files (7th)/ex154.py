# Exercise 154. Frequency of letters in a file

file_name = input("Input file name: ")
with open(file_name , "r") as file:
    letters_file = file.read()
    letters = []
    for letter in letters_file:
        if letter.isalnum():
            if letter.lower() not in letters:
                letters.append(letter.lower())
for letter in letters:
    print(letter ,"-", letters_file.count(letter))
file.close()