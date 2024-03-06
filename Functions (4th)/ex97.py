# Exercise 97: Operator precedence

def precedence(text):
    sings = {"+":1 , "-": 1, "*": 2, "/": 2, "^": 3}
    for i in text:
        if i in sings:
            return sings[i]
        else:
            print("You need to input one of this sings (+ , - , * , / , )")
            return 1
        

if __name__ == "__main__":
    text = input("Input here your text: ")

    print(precedence(text))