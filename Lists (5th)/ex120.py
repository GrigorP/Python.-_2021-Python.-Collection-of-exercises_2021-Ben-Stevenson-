# Exercise 120: Formatting a List

def formatting(list_of_words: list):
    result = ""
    if len(list_of_words) == 1:
        result = list_of_words
        result_str = " ".join(result)
    elif len(list_of_words) == 2:
        result = list_of_words.copy()
        result[-1] = "and"
        result.append(list_of_words[-1])
        result_str = " ".join(result)
    elif len(list_of_words) > 2:
        result = list_of_words.copy()
        for i in range(len(result)):
            if i < len(result) - 2:
                result[i] += ","
            elif i == len(result) - 2:
                result[i + 1] = "and"
        if result[-1] != list_of_words[-1]:
            result.append(list_of_words[-1])
        result_str = " ".join(result)
    else:
        result = "Enter words"

    return result_str
    
word = input("Input word(for example ` apples, oranges, bananas, lemons: blank for close): ")
list_of_words = []

while word:
    list_of_words.append(word)
    word = input("Input word(for example ` apples, oranges, bananas, lemons: blank for close): ")

print(formatting(list_of_words))
