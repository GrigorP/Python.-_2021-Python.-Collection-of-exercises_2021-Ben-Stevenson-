# Exercise 130. Unary and binary operators

import re

def tokenize(expression):
    operator_pattern = r'[-+*/^()]'
    number_pattern = r'\d+'

    combined_pattern = '|'.join([operator_pattern, number_pattern])

    tokens = re.findall(combined_pattern, expression)

    tokens = [token.strip() for token in tokens if token.strip()]

    return tokens

def replace_unary_operators(tokens):
    replaced_tokens = []
    for i, token in enumerate(tokens):
        if token == '+' or token == '-':
            if i == 0 or tokens[i - 1] in '+-*/^(':
                replaced_tokens.append('u' + token)
            else:
                replaced_tokens.append(token)
        else:
            replaced_tokens.append(token)
    return replaced_tokens

def main():
    expression = input("Enter a mathematical expression: ")
    tokens = tokenize(expression)
    unary_operators = [token for token in tokens if token in ('u+', 'u-')]
    replaced_tokens = replace_unary_operators(tokens)
    
    print("Original tokens:", tokens)
    print("Unary operators:", unary_operators)
    print("Tokens with replaced unary operators:", replaced_tokens)

if __name__ == "__main__":
    main()