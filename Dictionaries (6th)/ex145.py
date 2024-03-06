# Exercise 145. Erudite

def erudite(dct: dict , word: str):
    result = 0
    while word:
        for key , values in dct.items():
            if word[-1].lower() in values:
                result += key
        word = word[:-1]
    return result


dct = {
    1: "aeilnorstu",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz"
}

word = input("Input word: ")

print(erudite(dct , word))