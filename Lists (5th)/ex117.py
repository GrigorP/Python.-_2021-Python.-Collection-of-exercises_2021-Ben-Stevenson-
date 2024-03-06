# Exercise 117. Words only

def words_only(sentence: str):
    words = []
    word = ""
    for i in sentence:
        if i.isalpha():
            word += i
        else:
            if word:
                words.append(word)
            word = ""
    
    return words

sentence = input("Inpute sentece: ")
print(words_only(sentence))

