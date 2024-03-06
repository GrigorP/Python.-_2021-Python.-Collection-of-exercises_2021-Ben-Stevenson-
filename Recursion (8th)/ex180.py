# Exercise 180. Editing distance

def editingDist(word1: str  , word2: str):
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    else:
        cost = 0
        if word1[-1] != word2[-1]:
            cost = 1
        d1 = editingDist(word1[:-1] , word2) + 1
        d2 = editingDist(word1 , word2[:-1]) + 1
        d3 = editingDist(word1[:-1] , word2[:-1]) + cost
        return min(d1 , d2 , d3)
    

word1 = input("Input word: ")
word2 = input("Input word: ")

print(editingDist(word1 , word2))