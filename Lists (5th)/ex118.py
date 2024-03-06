# Exercise 118. Verbal palindromes

def verbal_palindromes(sentece):
    sentece_list = []
    word = ""
    result = False

    for i in sentence:
        if i.isalpha():
            word += i
        else:
            if word:
                sentece_list.append(word.lower())
            word = ""
    
    for i in range(len(sentece_list)):
        if sentece_list[i] == sentece_list[-(i + 1)]:
            result = True
        else:
            result = False
            return result
    return result

sentence = input("Input sentence: ")

print(verbal_palindromes(sentence))
