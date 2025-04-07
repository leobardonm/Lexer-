# lexer.py
# José Leobardo Navarro Márquez
# Regina Martinez Vázquez
# Implementación de métodos computacionales

import sys

# Definimos los tipos de tokens
class TokenType:
    ENTERO = "Entero"
    FLOAT = "Real"
    ASIGNACION = "Asignación"
    ADICION = "Suma"
    SUSTRACCION = "Resta"
    MULTIPLICACION = "Multiplicación"
    DIVISION = "División"
    POTENCIA = "Potencia"
    IDENTIFICADOR = "Variable"
    COMENTARIO = "Comentario"
    PARENTESIS = "Paréntesis"
    NUEVA_LINEA = "Nueva línea"

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
        
        # Comentario
        if char == '/' and current + 1 < len(text) and text[current + 1] == '/':
            comment = ""
            current += 2  # Saltamos los dos slashes
            while current < len(text) and text[current] != '\n':
                comment += text[current]
                current += 1
            tokens.append(Token(TokenType.COMENTARIO, f"//{comment}"))
            continue

        # Salto de línea
        if char == '\n':
            tokens.append(Token(TokenType.NUEVA_LINEA, char))
            current += 1
            continue

        # Espacio o tabulación
        if char.isspace():
            current += 1
            continue

        # Identificador
        if char.isalpha():
            identifier = ""
            while current < len(text) and (text[current].isalnum() or text[current] == '_'):
                identifier += text[current]
                current += 1
            tokens.append(Token(TokenType.IDENTIFICADOR, identifier))
            continue

        # Número (entero o real con/ sin notación exponencial)
        if char.isdigit() or (char == '.' and current + 1 < len(text) and text[current + 1].isdigit()) or \
           (char in '+-' and current + 1 < len(text) and (text[current + 1].isdigit() or text[current + 1] == '.')):
            number = ""
            has_dot = False
            has_e = False

            if char in '+-':
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
                    tokens.append(Token(TokenType.ENTERO, int(number)))
            except ValueError:
                print(f"⚠ Número mal formado: {number}")
            continue

        # Operadores y paréntesis
        if char == '=':
            tokens.append(Token(TokenType.ASIGNACION, char))
        elif char == '+':
            tokens.append(Token(TokenType.ADICION, char))
        elif char == '-':
            tokens.append(Token(TokenType.SUSTRACCION, char))
        elif char == '*':
            tokens.append(Token(TokenType.MULTIPLICACION, char))
        elif char == '/':
            tokens.append(Token(TokenType.DIVISION, char))
        elif char == '^':
            tokens.append(Token(TokenType.POTENCIA, char))
        elif char == '(' or char == ')':
            tokens.append(Token(TokenType.PARENTESIS, char))

        current += 1

    return tokens

def lexerAritmetico(archivo):
    with open(archivo, "r") as file:
        text = file.read()
    return lexer(text)

def print_tokens_by_line(tokens):
    for token in tokens:
        if token.type != TokenType.NUEVA_LINEA:
            print(f"\n{token.value}" + "    " + f"{token.type}\n")

# --- Punto de entrada ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python lexer.py archivo.txt")
    else:
        archivo = sys.argv[1]
        tokens = lexerAritmetico(archivo)
        print_tokens_by_line(tokens)
