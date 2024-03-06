# Exercise 129. Splitting a string into tokens

import re

def tokenize(expression):
    operator_pattern = r'[-+*/^()]'
    number_pattern = r'\d+'

    combined_pattern = '|'.join([operator_pattern, number_pattern])

    tokens = re.findall(combined_pattern, expression)

    tokens = [token.strip() for token in tokens if token.strip()]

    return tokens

def main():
    expression = input("Enter a mathematical expression: ")
    tokens = tokenize(expression)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()