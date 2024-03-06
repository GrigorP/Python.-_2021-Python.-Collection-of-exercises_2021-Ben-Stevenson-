# Exercise 142. Unique symbols

def uniqueSymbols(sentence: str):
    result = ""
    for i in sentence.lower():
        if i not in result:
            result += i
    return len(result)

sentence = input("Input sentence: ")

print(uniqueSymbols(sentence))