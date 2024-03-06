# Exercise 122. “Pig Latin”

vowels = 'aouei'

word = input("Input word: ")

if word[0] in vowels:
    word += "way"
else:
    for i in word:
        if i not in vowels:
            letter = word[0]
            word = word[1:]
            word += letter
        else:
            break
    word += "ay"

print(word)