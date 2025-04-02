#cant use libraries

class TokenType():
    INTEGER = "Entero"
    FLOAT = "Real"
    ASSIGNMENT = "Asignación"
    ADDITION = "Suma"
    SUBTRACTION = "Resta"
    MULTIPLICATION = "Multiplicación"
    DIVISION = "División"
    POWER = "Potencia"
    IDENTIFIER = "Identificador"
    COMMENT = "Comentario"
    OPERATOR = "Operador"
    PUNCTUATION = "Puntuación"
    SEPARATOR = "Separador"
    LEFT_PAREN = "Parentesis izquierdo"
    RIGHT_PAREN = "Parentesis derecho"
    NEWLINE = "Nueva linea"

class Token():
    type: TokenType
    value: any = None

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}: {self.value}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
     
