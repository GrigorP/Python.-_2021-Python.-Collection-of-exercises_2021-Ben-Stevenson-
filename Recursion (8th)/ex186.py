# Exercise 186: Run Length Coding

def decoding(word):
    if len(word) == 0:
        return []
    else:
        count_of_symbol = 0
        decoded_lst = [word[0]]
        symbol = word[0]
        while symbol == word[0]:
            count_of_symbol += 1
            word = word[1:]
            if len(word) == 0:
                break
        decoded_lst.append(count_of_symbol)
        return decoded_lst + decoding(word)

word = input("Input word: ")
print(decoding(word))