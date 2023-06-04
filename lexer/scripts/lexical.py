import re

# Regular expressions for token patterns
token_patterns = [
    (r'"[^"\\]*(?:\\.[^"\\]*)*"', 'STRING'),  # Strings within double quotes
    (r'[A-Za-z_][A-Za-z0-9_]*', 'IDENTIFIER'),  # Alphabets and underscore followed by alphanumeric characters
    (r'\d+', 'NUMBER'),  # Numbers
    (r'\(', 'LPAREN'),  # Left parenthesis
    (r'\)', 'RPAREN'),  # Right parenthesis
    (r'\{', 'LBRACE'),  # Left brace
    (r'\}', 'RBRACE'),  # Right brace
    (r'\[', 'LBRACKET'),  # Left bracket
    (r'\]', 'RBRACKET'),  # Right bracket
    (r'\+', 'PLUS'),  # Plus operator
    (r'-', 'MINUS'),  # Minus operator
    (r'\*', 'MULTIPLY'),  # Multiply operator
    (r'/', 'DIVIDE'),  # Divide operator
    (r'%', 'MODULUS'),  # Modulus operator
    (r'=', 'ASSIGN'),  # Assignment operator
    (r'==', 'EQUAL'),  # Equal to operator
    (r'\|\|', 'OR'),  # Logical OR operator
    (r'&&', 'AND'),  # Logical AND operator
    (r'<<', 'LEFT_SHIFT'),  # Left shift operator
    (r'>>', 'RIGHT_SHIFT'),  # Right shift operator
    (r'<', 'LESS_THAN'),  # Less than operator
    (r'>', 'GREATER_THAN'),  # Greater than operator
    (r'#', 'HASH'),  # Hash
    (r'\.', 'DOT'),  # Dot
    (r'\+\+', 'INCREMENT'),  # Increment operator
    (r'--', 'DECREMENT'),  # Decrement operator
    (r';', 'SEMICOLON'),  # Semicolon
]

# Regular expression for strings within double quotes
string_pattern = r'"[^"\\]*(?:\\.[^"\\]*)*"'

# Regular expression for single-line comments
single_line_comment_pattern = r'//.*'

# Regular expression for multi-line comments
multi_line_comment_pattern = r'/\*[\s\S]*?\*/'


def tokenize_cpp_code(code):
    # Remove spaces, newlines, and tabs
    code = re.sub(r'\s+', '', code)

    # Remove single-line comments
    code = re.sub(single_line_comment_pattern, '', code)

    # Remove multi-line comments
    code = re.sub(multi_line_comment_pattern, '', code)

    tokens = []
    while code:
        matched = False
        if code[0] == '"':
            match = re.match(string_pattern, code)
            if match:
                value = match.group()
                tokens.append(('STRING', value))
                code = code[len(value):]
                matched = True

        if not matched:
            for pattern, token_type in token_patterns:
                match = re.match(pattern, code)
                if match and match.start() == 0:
                    value = match.group()
                    tokens.append((token_type, value))
                    code = code[len(value):]
                    matched = True
                    break

        if not matched:
            tokens.append(('INVALID', code[0]))
            code = code[1:]

    return tokens


# Example usage
cpp_code = '''
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    bool flag = true;
    if (flag) {
        cout << "Hello, World!" << endl;
    }
    // This is a single-line comment
    /*
    This is a
    multi-line comment
    */
    return 0;
}
'''

tokens = tokenize_cpp_code(cpp_code)
for token_type, value in tokens:
    print(f'{token_type}: {value}')
