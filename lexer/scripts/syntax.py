# Import the tokenize function from the lexer.py file
from lexical import tokenize

# Syntax analyzer
def analyze_syntax(tokens):
    # Check if the code starts with 'int main()'
    if tokens.pop(0) != ('KEYWORD', 'int') or tokens.pop(0) != ('IDENTIFIER', 'main') or tokens.pop(0) != ('LPAREN', '(') or tokens.pop(0) != ('RPAREN', ')'):
        return False

    # Check if the code is enclosed in braces {}
    if tokens.pop(0) != ('LBRACE', '{'):
        return False

    # Check for valid statements inside the main function
    while len(tokens) > 0:
        token = tokens.pop(0)
        print("Token: ",token)
        # Check for variable declarations
        if token[0] == 'KEYWORD' and token[0] in ['int', 'bool']:
            if tokens.pop(0)[0] != 'IDENTIFIER':
                return False
            if tokens.pop(0) == ('ASSIGN', '='):
                if tokens.pop(0)[0] != 'NUMBER':
                    return False
            if tokens.pop(0) != ('SEMICOLON', ';'):
                return False

        # Check for if statements
        elif token == ('KEYWORD', 'if'):
            if tokens.pop(0) != ('LPAREN', '('):
                return False
            if not (tokens.pop(0)[0] == 'IDENTIFIER' or tokens[0][0] == 'NUMBER'):
                return False
            if tokens.pop(0) not in [('LESS_THAN', '<'), ('GREATER_THAN', '>'), ('EQUALS', '=')]:
                return False
            if not (tokens.pop(0)[0] == 'IDENTIFIER' or tokens[0][0] == 'NUMBER'):
                return False
            if tokens.pop(0) != ('RPAREN', ')'):
                return False
            if tokens.pop(0) != ('LBRACE', '{'):
                return False
            braces_count = 1
            while braces_count > 0:
                if tokens[0] == ('LBRACE', '{'):
                    braces_count += 1
                elif tokens[0] == ('RBRACE', '}'):
                    braces_count -= 1
                tokens.pop(0)

        # Check for cout statements
        elif token == ('IDENTIFIER', 'cout'):
            while tokens[0][0] != 'SEMICOLON':
                if tokens.pop(0) == ('LESS_THAN', '<') and tokens.pop(0) != ('LESS_THAN', '<'):
                    return False
                tokens.pop(0)
            tokens.pop(0)

        # Check for single-line or multi-line comments
        elif token == ('HASH', '//'):
            while tokens[0][0] != 'SEMICOLON':
                tokens.pop(0)
            tokens.pop(0)

        elif token == ('HASH', '/*'):
            while (tokens[0][0], tokens[1][0]) != ('HASH', '*/'):
                tokens.pop(0)
            tokens.pop(0)
            tokens.pop(0)

        # Check for the end of the main function
        elif token == ('RBRACE', '}'):
            if len(tokens) > 0:
                return False

    # Code is valid if it reaches this point
    return True

# Test inputs
inputs = [
    'int main()\n{\n    int a = 10;\n    if(a>10)\n    {\n        cout<<"Hello World"<<endl;\n    }\n    return 0;\n}',
    'int main() {\n    int x = 10;\n    bool flag = true;\n    if (flag) {\n        cout << "Hello, World!" << endl;\n    }\n    // This is a single-line comment\n    /*\n    This is a\n    multi-line comment\n    */\n\ta++;\n    return 0;\n}',
    'while(x>10)\n{\na = b+5;\nif(a>69)\n{\na=b-5;\n}\n}'
]

for i, code in enumerate(inputs):
    tokens = tokenize(code)
    if analyze_syntax(tokens):
        print("Valid\n")
    else:
        print("Invalid\n")