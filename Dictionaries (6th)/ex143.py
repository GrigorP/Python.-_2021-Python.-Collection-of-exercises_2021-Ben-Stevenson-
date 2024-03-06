# Exercise 143. Anagrams

def are_anagrams(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()
    
    return sorted(word1) == sorted(word2)

word1 = input("Input first word: ")
word2 = input("Input second word: ")

print(are_anagrams(word1, word2))