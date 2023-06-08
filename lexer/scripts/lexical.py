import re

# Regular expression patterns for tokens
patterns = [
    ('IF', r'if'),  # IF
    ('ELSE', r'else'),  # ELSE
    ('DO', r'do'),  # DO
    ('WHILE', r'while'),  # WHILE
    ('FOR', r'for'),  # FOR
    ('SWITCH', r'switch'),  # SWITCH
    ('CASE', r'case'),  # SWITCH
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Alphabets and underscore followed by alphanumeric characters
    ('NUMBER', r'\d+'),  # Numbers
    ('STRING', r'\"([^\\\n]|(\\.))*?\"'),  # Strings within double quotes
    ('INCREMENT', r'\+\+'),  # Increment operator
    ('DECREMENT', r'--'),  # Decrement operator
    ('PLUS', r'\+'),  # Plus operator
    ('MINUS', r'-'),  # Minus operator
    ('MULTIPLY', r'\*'),  # Multiply operator
    ('DIVIDE', r'/'),  # Divide operator
    ('MODULUS', r'%'),  # Modulus operator
    ('EQUALS', r'='),  # Equal to operator
    ('SEMICOLON', r';'),  # Semicolon
    ('COLON', r':'),  # Colon
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('LBRACE', r'{'),  # Left brace
    ('RBRACE', r'}'),  # Right brace
    ('LBRACKET', r'\['),  # Left bracket
    ( 'RBRACKET', r'\]'),  # Right bracket
    ('ASSIGN', r'='),  # Assignment operator
    ('OR', r'\|\|'),  # Logical OR operator
    ('AND', r'&&'),  # Logical AND operator
    ('LEFT_SHIFT', r'<<'),  # Left shift operator
    ('RIGHT_SHIFT', r'>>'),  # Right shift operator
    ('LESS_THAN', r'<'),  # Less than operator
    ('GREATER_THAN', r'>'),  # Greater than operator
    ('HASH', r'#'),  # Hash
    ('DOT', r'\.'),  # Dot
]

# List of reserved words in C++
reserved_words = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit', 'atomic_noexcept',
    'auto', 'bitand', 'bitor', 'bool', 'break', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t',
    'class', 'compl', 'concept', 'const', 'consteval', 'constexpr', 'constinit', 'const_cast', 'continue',
    'co_await', 'co_return', 'co_yield', 'decltype', 'default', 'delete', 'double', 'dynamic_cast',
    'enum', 'explicit', 'export', 'extern', 'false', 'float', 'friend', 'goto', 'iostream', 
    'include', 'inline', 'int', 'long', 'main', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr', 
    'operator', 'or', 'or_eq', 'private', 'protected', 'public', 'reflexpr', 'register', 'reinterpret_cast', 
    'requires', 'return', 'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'std', 'struct', 
    'synchronized', 'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 
    'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'xor', 'xor_eq'
]

# Tokenize the code
def tokenize(code):
    tokens = []
    position = 0
    total_length = len(code)

    while position < total_length:
        match = None

        # Skip spaces, new lines, and tabs
        if re.match(r'\s', code[position]):
            position += 1
            continue

        # Skip single-line comments
        if code[position:position+2] == '//':
            position = code.find('\n', position)
            if position == -1:
                break
            continue

        # Skip multi-line comments
        if code[position:position+2] == '/*':
            position = code.find('*/', position+2)
            if position == -1:
                break
            position += 2
            continue

        # Match reserved words
        for reserved_word in reserved_words:
            regex = re.compile(r'\b' + re.escape(reserved_word) + r'\b')
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                token = ('KEYWORD', value)
                tokens.append(token)
                position = match.end()
                break

        if not match:
            for token_name, pattern in patterns:
                regex = re.compile(pattern)
                match = regex.match(code, position)
                if match:
                    value = match.group(0)
                    token = (token_name, value)
                    tokens.append(token)
                    position = match.end()
                    break

        if not match:
            print("Illegal character '%s'" % code[position])
            position += 1

    return tokens