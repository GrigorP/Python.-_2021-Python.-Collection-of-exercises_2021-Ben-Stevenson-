# Exercise 178. Recursive palindromes

def recPolind(word: str):
    if word == "":
        return True
    if len(word) >= 2:
        if word[0] == word[-1]:
            return recPolind(word[1:-1])
    if len(word) == 1:
        return True
    else:
        return False

word = input("Input word: ")
print(recPolind(word))