# lexer.py
# José Leobardo Navarro Márquez
# Regina Martinez Vázquez
# Implementacion de metodos computacionales


#Definimos los tipos de tokens
class TokenType:
    INTEGER = "Entero"
    FLOAT = "Real"
    ASSIGNMENT = "Asignación"
    ADDITION = "Suma"
    SUBTRACTION = "Resta"
    MULTIPLICATION = "Multiplicación"
    DIVISION = "División"
    POWER = "Potencia"
    IDENTIFIER = "Variable"
    COMMENT = "Comentario"
    LEFT_PAREN = "Paréntesis izquierdo"
    RIGHT_PAREN = "Paréntesis derecho"
    NEWLINE = "Nueva línea"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}: {self.value}"
    
    def __repr__(self):
        return self.__str__()

def lexer(text):
    tokens = []
    current = 0
    text = text.strip()
    
    while current < len(text):
        char = text[current]
        
        #  Revisa si hay un comentario
        if char == '/' and current + 1 < len(text) and text[current + 1] == '/':
            comment = ""
            while current < len(text) and text[current] != '\n':
                comment += text[current]
                current += 1
            tokens.append(Token(TokenType.COMMENT, comment))
            continue

        # Revisa si hay un salto de linea
        if char == '\n':
            tokens.append(Token(TokenType.NEWLINE, char))
            current += 1
            continue

        # Revisa si hay un espacio en blanco
        if char.isspace():
            current += 1
            continue

        # Revisa si hay un identificador
        if char.isalpha():
            identifier = ""
            while current < len(text) and (text[current].isalnum() or text[current] == '_'):
                identifier += text[current]
                current += 1
            tokens.append(Token(TokenType.IDENTIFIER, identifier))
            continue

        # Revisa si hay un numero
        if char.isdigit() or (char == '.' and current + 1 < len(text) and text[current + 1].isdigit()) or \
           (char in '+-' and current + 1 < len(text) and (text[current + 1].isdigit() or text[current + 1] == '.')):
            number = ""
            has_dot = False
            has_e = False

            if char in '+-': #Revisa si hay un signo mas o menos y lo agrega al numero
                number += char
                current += 1
                char = text[current] if current < len(text) else ''

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

            try:
                if has_dot or has_e:
                    tokens.append(Token(TokenType.FLOAT, float(number)))
                else:
                    tokens.append(Token(TokenType.INTEGER, int(number)))
            except ValueError:
                print(f"⚠ Número mal formado: {number}")
            continue

        # Revisa si hay un operador
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

        current += 1

    return tokens

def print_tokens_by_line(tokens):
    for token in tokens:
        if token.type != TokenType.NEWLINE:
            print(f"\n{token.value}\n\n{token.type}\n")

# --- Punto de entrada ---
if __name__ == "__main__":
    with open("input_example.txt", "r") as file:
        text = file.read()
        tokens = lexer(text)
        print_tokens_by_line(tokens)
