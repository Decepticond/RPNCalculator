import operator
from themath import *


"""

Author: Aleksandr S
Date Modified: June 18th, 2023.
Description: This file (RPN.py) uses the shunting yard algorithim, utilizing the precedences in order to get the correct (BEDMAS) order of operations. This also uses the
operators module to organize the operators and make it easier to utilize them, alongsidie the themath module that I made in place of the math module.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

** Function 1 **
tokenizeExpression- This function takes an expression argument and tokenizes it into a list of tokens. It iterates over each character in 
the expression and builds tokens based on digits, decimal points, operators, and parentheses. The tokens are stored in a list and returned at the end.


 * Variables *
 expression = The input expression to be tokenized.
 tokens = A list to store the tokens extracted from the expression.
 currentToken = A string to accumulate characters and build a token.
 count = An integer to keep track of the current character position in the expression.
 expressToken = A string to accumulate characters and build a token for operators.
 char = A variable to iterate over each character in the expression.

 * Input *
 expression: The input expression to be tokenized.

 * Output *
 tokens: The list of tokens extracted from the expression.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

** Function 2 **
calculateRPN - This function evaluates an expression in Reverse Polish Notation via the shunting yard algorithim using the provided operators and variables.

 * Variables *
 expression = The input expression in RPN.
 variables = A dictionary of variables and their corresponding values (default: None).
 operators = A set of supported operators.
 tokens = A list of tokens extracted from the expression.
 token = The current token being processed.
 stack = A stack to store processing results during the evaluation process.
 Precedence = A dictionary that maps operators to their precedence levels.
 operand1 = The first operand in the binary operation.
 operand2 = The second operand in the binary operation.

 * Input *
 expression: The input expression in RPN.
 variables: A dictionary of variables and their corresponding values (default: None).

 * Output *
 The evaluated result of the expression.
 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *



"""


OPERATORS = {

    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    'sin': MySin,
    'cos': MyCos,
    'tan': MyTan,
    'log': MyLog10

}


def tokenizeExpression(expression):

    tokens = []
    currentToken = ""
    count = 0
    expressToken = ""

    for char in expression:
        if char.isdigit() or char == '.':
            currentToken += char

        elif currentToken:
            tokens.append(currentToken)
            currentToken = ""

        elif expressToken in OPERATORS.keys():
            tokens.append(expressToken)
            expressToken = ""

        if char in OPERATORS.keys() or char in "()" and char not in ['x', 'y', 'z']:
            tokens.append(char)

        else:
            expressToken += char
        count += 1

    if currentToken:
        tokens.append(currentToken)

    return tokens


def calculateRPN(expression, variables=None):
    if variables is None:
        variables = {}

    operators = set(OPERATORS.keys())
    tokens = tokenizeExpression(expression)
    output = []
    stack = []

    Precedence = {

        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        'sin': 4,
        'cos': 4,
        'tan': 4,
        'log': 4

    }

    for token in tokens:

        try:
            output.append(float(token))
        except ValueError:

            if token in variables:
                output.append(variables[token])

            elif token in OPERATORS or token == '*':
                while stack and stack[-1] != '(' and (
                        token in ['+', '-', '-', 'sin', 'cos', 'tan', 'log'] or Precedence[token] < Precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(token)

            elif token == '(':
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())

                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                raise ValueError("Invalid token: {}".format(token))

    while stack:
        output.append(stack.pop())

    stack = []

    for token in output:
        if isinstance(token, float):
            stack.append(token)

        elif token in operators or token == '*':
            if token in ['sin', 'cos', 'tan', 'log']:
                if len(stack) < 1:
                    raise ValueError("Invalid expression")
                operand = stack.pop()
                result = OPERATORS[token](operand)
                stack.append(result)

            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '/' and operand2 == 0:
                    raise ZeroDivisionError("float division by zero")
                result = OPERATORS[token](operand1, operand2)
                stack.append(result)
                
        else:
            raise ValueError("Invalid token: {}".format(token))

    return stack[0] if stack else None


