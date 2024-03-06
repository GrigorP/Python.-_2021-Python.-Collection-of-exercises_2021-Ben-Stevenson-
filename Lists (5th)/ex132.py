# Exercise 132: Executing Postfix Expressions

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

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    elif operator == 'u+' or operator == 'u-':
        return 4  # Higher precedence for unary operators
    else:
        return 0  # Lowest precedence for other tokens

def infix_to_postfix(tokens):
    operators = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in ('+', '-', '*', '/', '^', 'u+', 'u-'):
            while operators and operators[-1] != '(' and precedence(token) <= precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()  # Discard the '('

    while operators:
        postfix.append(operators.pop())

    return postfix

def evaluate_postfix(postfix_expression):
    values = []

    for token in postfix_expression:
        if token.isdigit():
            values.append(int(token))
        elif token == 'u-':
            operand = values.pop()
            values.append(-operand)
        elif token == 'u+':
            operand = values.pop()
            values.append(operand)
        else:
            right = values.pop()
            left = values.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left ** right
            values.append(result)

    return values[0]

def main():
    infix_expression = input("Enter a mathematical expression in infix form: ")
    tokens = tokenize(infix_expression)
    tokens_with_unary = replace_unary_operators(tokens)
    postfix_expression = infix_to_postfix(tokens_with_unary)
    print("Postfix expression:", postfix_expression)
    result = evaluate_postfix(postfix_expression)
    print("Result:", result)

if __name__ == "__main__":
    main()