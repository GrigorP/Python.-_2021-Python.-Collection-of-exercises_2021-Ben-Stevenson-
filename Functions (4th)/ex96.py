# Exercise 96. Is the string an integer?

def isInteger(your_string: str):
    your_string = your_string.strip()
    signs = ["+" , "-" , "*" , "/" , "%" , "^" , " "]
    for i in your_string:
        if i.isalpha():
            return False
        if i in signs:
            your_string = your_string.replace(i , "")
    print(your_string)
    if int(your_string):
        return True
    else:
        return False
    

if __name__ == "__main__":
    your_string = input("Input your string: ")
    print(isInteger(your_string))
    
