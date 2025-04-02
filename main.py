from tokens import Token, TokenType

def lexer(text):
    tokens = []
    current = 0
    text = text.strip()
    
    while current < len(text):
        char = text[current]
        
        # Maneja los saltos de linea
        if char == '\n':
            tokens.append(Token(TokenType.NEWLINE, char))
            current += 1
            continue
            
        # Saltea los espacios en blanco|
        if char.isspace():
            current += 1
            continue
            
        # Maneja los identificadores (variables)
        if char.isalpha():
            identifier = ""
            while current < len(text) and (text[current].isalnum() or text[current] == '_'):
                identifier += text[current]
                current += 1
            tokens.append(Token(TokenType.IDENTIFIER, identifier))
            continue
            
        # Maneja los numeros enteros y los reales
        if char.isdigit() or char == '.':
            number = ""
            has_dot = False
            has_e = False
            #Prueba que el numero sea valido en formato de punto flotante
            while current < len(text):
                char = text[current]
                if char.isdigit():
                    number += char
                elif char == '.' and not has_dot:
                    number += char
                    has_dot = True
                elif char in 'eE' and not has_e:
                    number += char
                    has_e = True
                elif char in '+-' and has_e and number[-1] in 'eE':
                    number += char
                else:
                    break
                current += 1
                
            if has_dot or has_e: 
                tokens.append(Token(TokenType.FLOAT, float(number)))
            else:
                tokens.append(Token(TokenType.INTEGER, int(number)))
            continue
            
        # Handle operators and special characters
        if char == '=':
            tokens.append(Token(TokenType.ASSIGNMENT, char))
        elif char == '+':
            tokens.append(Token(TokenType.ADDITION, char))
        elif char == '-':
            tokens.append(Token(TokenType.SUBTRACTION, char))
        elif char == '*':
            tokens.append(Token(TokenType.MULTIPLICATION, char))
        elif char == '/':
            tokens.append(Token(TokenType.DIVISION, char))
        elif char == '^':
            tokens.append(Token(TokenType.POWER, char))
        elif char == '(':
            tokens.append(Token(TokenType.LEFT_PAREN, char))
        elif char == ')':
            tokens.append(Token(TokenType.RIGHT_PAREN, char))
            
        # Handle comments
        if char == '/' and current + 1 < len(text) and text[current + 1] == '/':
            comment = ""
            while current < len(text) and text[current] != '\n':
                comment += text[current]
                current += 1
            tokens.append(Token(TokenType.COMMENT, comment))
            continue
            
        current += 1
        
    return tokens

def print_tokens_by_line(tokens):
    current_line = []
    for token in tokens:
        if token.type == TokenType.NEWLINE:
            print(current_line)
            current_line = []
        else:
            current_line.append(token)
    if current_line:
        print("Line tokens:", current_line)

# Test the lexer
with open("input_example.txt", "r") as file:
    text = file.read()
    tokens = lexer(text)
    print_tokens_by_line(tokens)