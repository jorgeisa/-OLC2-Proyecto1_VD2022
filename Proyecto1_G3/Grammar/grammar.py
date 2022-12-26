'''
Grupo 3 :^)
'''


reserved = {
    'print' :   'RPRINT',    
    # Comienzan Tipos Basico
    'None'  :   'RNONE',
    'int'   :   'RINT',
    'float' :   'RFLOAT',
    'bool'  :   'RBOOL',
    'string':   'RSTRING',
    'False' :   'RFALSE',
    'True'  :   'RTRUE',
    # Terminan Tipos Basicos
    # Comienzan Tipos Compuestos
    'list'  :   'RLIST',
    'struct':   'RSTRUCT'
    # Terminan Tipos Compuestos
}

tokens = [
    # Comments
    "COMMENUNI",
    "COMMENMUL",

    "SALTOLINEA",
    "DOSPUNTOS",
    "PARIZQ",
    "PARDER",
    'COMA',

    "CADENA",
    'ID',
    
    # Empieza Aritmeticas     
    'EQUALS',
    'PLUS',
    'MINUS',
    'POR',
    'DIVIDE',
    'MODULATE',
    'POT',
    # Termina Aritmeticas

    'FLOAT',
    'INTEGER',

    # Empiezan Relacionales
    # Operadores Relacionales
    'EQUALIZATIONSIGN',  # Signo de Igualacion
    'DIFFERENTIATIONSIGN',  # Signo de diferenciacion
    'SMALLERTHAN',      # Signo de Menor que
    'GREATERTHAN',      # Signo de Mayor que
    'LESSEQUAL',        # Signo de Menor Igual
    'GREATEREQUAL'     # Signo de Mayor Igual
    # Terminan Relacionales
    
    

] + list(reserved.values())

# Tokens Definitions
t_SALTOLINEA = r'\n'
t_DOSPUNTOS = r':'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_COMA = r'\,'
# Empiezan Operadores Relacionales
t_EQUALIZATIONSIGN = r'=='
t_DIFFERENTIATIONSIGN = r'!='
t_SMALLERTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
# Terminan Operadores Relacionales
# Empiezan Aritmeticas
t_EQUALS    = r'\='
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_POR       = r'\*'
t_DIVIDE    = r'\/'
t_MODULATE  = r'\%'
t_POT      = r'\*\*'
# Terminan Aritmeticas



# Comentario Unilinea
def t_COMMENUNI(t):
    r'\#\=(.|\n)*?\=\#'
    t.lexer.lineno += t.value.count('\n')
# Termina Comentario Unilinea

# Empieza Comentario Multilinea
def t_COMMENMUL(t):
    r'\#.*\n'
    t.lexer.lineno += 1
# Termina Comentario Unilinea

# Empieza Float  
def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("FLOAT VALUE ERROR TO LARGE %d",t.value)
        t.value = 0
    return t

# Empieza Int
def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("INTEGER VALUE ERROR %d",t.value)
        t.value = 0
    return t

# Empieza ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # revisar en la lista de reservadas
    return t

# Empieza Cadena
def t_CADENA(t):
    # r'\"(\\"|.)*?\"'
    r"""\"(\\"|\\'|\\\\|\\n|\\t|\\r|[^\\\'\"])*?\""""
    t.value = t.value[1:-1]  # remover comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t

# Ignored character
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Lexic Errors
def t_error(t):
    print("Ilegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.lex as lex
lexer = lex.lex()

# Empiezan Imports Gramatica
from Proyecto1_G3.Abstract.Return import Type
from Proyecto1_G3.Expression.Literal import Literal
from Proyecto1_G3.Expression.Access import Access
from Proyecto1_G3.Expression.Relational import Relational, RelationalOption

from Proyecto1_G3.Instruction.Native.Print import Print
from Proyecto1_G3.Instruction.Declaration import Declaration
# Terminan Imports Gramatica

# Empieza Precedencia
'''precedence =(
    (),
    (),
    (),
    (),
    (),


)'''
# Termina precedencia 

# Init List of Instructions
def p_init(t):
    'init     : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

# Instructions 

def p_instruccion(t):
    '''instruccion      : print_instr finins
                        | asignacion_instr  finins
                        | definicion_asignacion_instr finins
    '''
    t[0] = t[1]

def p_finins(t):
    '''finins       : SALTOLINEA
                    | '''
    t[0] = None

# Produccion Error
def p_instruccion_error(t):
    'instruccion  : error finins'
    print("ERROR - ", "Error Sintáctico. Instruccion " + str(t[1].value), t.lineno(1), find_column(input, t.slice[1]))
    t[0] = ""

# Empieza Print
def p_print_instr(t):
    'print_instr  : RPRINT PARIZQ expres_lista PARDER'
    t[0] = Print(t[3], t.lineno(1), find_column(input, t.slice[1]), False)

# Empieza Asignacion
def p_asignacion_instr(t):
    'asignacion_instr  : ID EQUALS expresion' 
    t[0] = Declaration(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_definicion_asginacion(t):
    'definicion_asignacion_instr  : ID  DOSPUNTOS tipo EQUALS expresion'
    t[0] = Declaration(t[1], t[5], t.lineno(1), find_column(input, t.slice[1]))

# Empieza Expresion Binaria Aritmetica
def p_expresion_binaria(t):
    '''
    expresion   :   expresion PLUS      expresion
                |   expresion MINUS     expresion
                |   expresion POR       expresion
                |   expresion DIVIDE    expresion
                |   expresion MODULATE  expresion
    '''
    if   t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]    
    elif t[2] == '%': t[0] = t[1] % t[3]

# Empieza Expresion Binaria Relacional
def p_expresion_binaria_relacional(t):
    '''
    expresion   :   expresion EQUALIZATIONSIGN      expresion
                |   expresion DIFFERENTIATIONSIGN     expresion
                |   expresion SMALLERTHAN       expresion
                |   expresion GREATERTHAN    expresion
                |   expresion LESSEQUAL  expresion
                |   expresion GREATEREQUAL  expresion
    '''
    if   t[2] == '==': 
        t[0] = Relational(t[1], t[3], RelationalOption.EQUAL, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=': 
        t[0] = Relational(t[1], t[3], RelationalOption.DISTINCT, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<': 
        t[0] = Relational(t[1], t[3], RelationalOption.LESS, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>': 
        t[0] = Relational(t[1], t[3], RelationalOption.GREATER, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=': 
        t[0] = Relational(t[1], t[3], RelationalOption.LESSEQUAL, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=': 
        t[0] = Relational(t[1], t[3], RelationalOption.GREATEREQUAL, t.lineno(2), find_column(input, t.slice[2]))
# Termina Expresion Binaria Relacional

# Empieza Lista Expresiones
def p_expresion_lista(t):
    '''expres_lista  : expres_lista COMA expresion
                     | expresion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

# Empieza Expresion Agrupacion
def p_expresion_agrupacion(t):
    'expresion  :   PARIZQ expresion PARDER'
    t[0] = t[2]

# Empieza Expresion Cadena
def p_expresion_cadena(t):
    'expresion  : CADENA'
    t[0] = Literal(str(t[1]), Type.STRING, t.lineno(1), find_column(input, t.slice[1]))

# Empieza Expresion Booleanos
def p_expresion_booleanos(t):
    '''expresion  : RTRUE
                  | RFALSE'''
    if t.slice[1].type == "RTRUE":
            t[0] = Literal(True, Type.BOOL, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == "RFALSE":
            t[0] = Literal(False, Type.BOOL, t.lineno(1), find_column(input, t.slice[1]))

# Empieza Expresion ID
def p_expresion_id(t):
    'expresion  :   ID'
    t[0] = Access(t[1], t.lineno(1), find_column(input, t.slice[1]))

# Empieza Tipo 
def p_tipo(t):
    '''
    tipo    : INTEGER
            | FLOAT
    '''
    t[0] = t[1]

# Empieza Expresion Numero
def p_expresion_number(t):
    '''
    expresion   :   INTEGER
                |   FLOAT
    '''
    if t.slice[1].type == "INTEGER":
        print("ES un entero")
        t[0] = Literal(t[1], Type.INT, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == "FLOAT":
        print("ES UN FLOAT")
        t[0] = Literal(t[1], Type.FLOAT, t.lineno(1), find_column(input, t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()

from Proyecto1_G3.SymbolTable.Generator import Generator
from Proyecto1_G3.SymbolTable.Environment import Environment

input = ''

def eject():
    s = ''
    with open('Proyecto1_G3/ArchivosPrueba/archivo.txt', 'r') as f:
        content = f.readlines()
        for element in content:
            s += element

    global input
    input = s
    print("\n\nEl input es: [\n" + input + "\n]\n\n")

    gen_aux = Generator()
    gen_aux.clean_all()
    generator = gen_aux.get_instance()
    new_env = Environment(None)
    
    instrucciones = parser.parse(input)

    for instruccion in instrucciones:
        if instruccion == None:
            print("Error En Gramatica xd")
        else:
            instruccion.compile(new_env)

    C3D = generator.get_code()
    f = open("salida.go", 'w')
    f.write(C3D)
    f.close()
    generator.clean_all()
    print(C3D)

def ejectText(inputText):
    
    global input
    input = inputText

    gen_aux = Generator()
    gen_aux.clean_all()
    generator = gen_aux.get_instance()
    new_env = Environment(None)
    
    instrucciones = parser.parse(input)

    for instruccion in instrucciones:
        if instruccion == None:
            print("Error")
            return ""
        else:
            instruccion.compile(new_env)

    C3D = generator.get_code()
    f = open("salida.go", 'w')
    f.write(C3D)
    f.close()
    # generator.clean_all()
    return generator
            
