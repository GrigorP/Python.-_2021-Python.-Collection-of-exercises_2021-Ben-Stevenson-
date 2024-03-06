# Exercise 140. Postal codes

def postalCodes(dct: dict , post_index: str):
    result = ""
    post_index = post_index.lower()
    if post_index[0] in dct:
        if post_index[0].isalpha() and post_index[1].isdigit():
            if post_index[0] != "x":
                result = dct[post_index[0]]
            else:
                result += dct[post_index[0]]
        else:
            if post_index[0].isalpha():
                result = "Second symbol must be number."
            else:
                result = "Wrong symbol."
    else:
        result = "Wrong symbol."
    return result

dct = {
    "a": "Newfoundland",
    "b": "Nova Scotia",
    "c": "Prince Edward Island",
    "e": "New Brunswick",
    "g": "Quebec",
    "h": "Quebec",
    "j": "Quebec",
    "k": "Ontario",
    "l": "Ontario",
    "m": "Ontario",
    "n": "Ontario",
    "p": "Ontario",
    "r": "Manitoba",
    "s": "Saskatchewan",
    "t": "Alberta",
    "v": "British Columbia",
    "x": "Nunavut or Northwest Territories",
    "y": "Yukon"
}

post_index = input("Input Your post index: ")

print(postalCodes(dct , post_index))
    