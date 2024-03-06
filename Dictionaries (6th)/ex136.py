# Exercise 136. Search by value

def reverseLookup(dct: dict , value_for_search):
    result = []
    for key , value in dct.items():
        if value == value_for_search:
            result.append(key)
    return result

dct = {
    "A": 1,
    "B": 1,
    "C": 1,
    "D": 2,
    "E": 3,
}

print(reverseLookup(dct , 1))