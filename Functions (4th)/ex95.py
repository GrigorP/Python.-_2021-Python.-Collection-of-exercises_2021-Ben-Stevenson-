# Exercise 95. Let's name the letters

def nameing(text):
    new_text = text[0].capitalize()

    for i in range(1, len(text)):
        if text[i] != "i":
            new_text += text[i]
        else:
            if text[i] == "i":
                if i != text[0]:
                    if str(text[i - 1]).isalpha() or str(text[i + 1]).isalpha():
                        new_text += 'i'
                    else:
                        new_text += 'I'
                else:
                    if str(text[i + 1]).isalpha():
                        new_text += 'I'

    return new_text

your_string = input("Input your string: ")

print(nameing(your_string))
