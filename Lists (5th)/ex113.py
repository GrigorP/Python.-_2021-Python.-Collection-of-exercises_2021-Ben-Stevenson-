# Exercise 113. Getting rid of duplicates

word = input("Input word(blank for close): ")
words = []

while word:
    if word not in words:
        words.append(word)
    word = input("Input word(blank for close): ")

print(words)
