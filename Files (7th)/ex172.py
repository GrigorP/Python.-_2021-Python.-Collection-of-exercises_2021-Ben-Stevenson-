# Exercise 172. Words with six vowels in a row

def sixVowels(filename):
    file = open(filename, "r")
    words = file.read().split()
    countt = 0
    sixvowwords = []
    for word in words:
        if "aeiouy" in word.lower():
            countt += 1
            sixvowwords.append(word)
    return countt , sixvowwords

filename = input("Input filename: ")
num , words = sixVowels(filename)

print(num , words)