# Exercise 144. Anagrams again

def anagrams(sentence1: str, sentence2: str) -> bool:
    sentence1 = sentence1.replace(" ", "").lower()
    sentence2 = sentence2.replace(" ", "").lower()
    print(sorted(sentence1))
    print(sorted(sentence2))

    return sorted(sentence1) == sorted(sentence2)

sentence1 = input("Input sentence: ")
sentence2 = input("Input sentence: ")

print(anagrams(sentence1, sentence2))