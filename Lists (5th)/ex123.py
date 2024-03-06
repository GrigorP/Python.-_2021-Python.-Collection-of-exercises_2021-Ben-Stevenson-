# Exercise 123. “Pig Latin” (continued)

vowels = 'aouei'

word = input("Input word: ")

if word[0].lower() in vowels:
    word += "way"
else:
    character = ""
    for i in word:
        if not word[-1].isalnum():
            character = word[-1]
            word = word.replace(word[-1] , "" , 1)
        if i not in vowels:
            letter = word[0].lower()
            if word[0] != word[0].capitalize():
                word = word[1:].capitalize()
            else:
                word = word[1:]
            word += letter
        else:
            break
    word += "ay"
    if character:
        word += character
print(word)