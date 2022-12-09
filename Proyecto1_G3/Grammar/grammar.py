import sys

reserved = {
    'print' : 'RPRINT'
}

tokens = [
    "SALTOLINEA",
    "PARIZQ",
    "PARDER",
    "CADENA",
    'ID',
] + list(reserved.values())

# Tokens Definitions
t_SALTOLINEA = r'\n'
t_PARIZQ = r'\('
t_PARDER = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')  # revisar en la lista de reservadas
    return t

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


# Grammar definition

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

# Instructions Options

def p_instruccion(t):
    'instruccion      : print_instr finins'
    t[0] = t[1]

def p_finins(t):
    '''finins       : SALTOLINEA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    'instruccion  : error SALTOLINEA'
    t[0] = "Error: " + str(t[1].value) + " - " + t.lineno(1) + " - " + find_column(input, t.slice[1])

# Expressions Options

def p_print_instr(t):
    'print_instr  : RPRINT PARIZQ expresion PARDER'
    t[0] = "Print Reconocido - " + t[3]

def p_expresion_cadena(t):
    'expresion  : CADENA'
    t[0] = "Cadena Reconocida: " + t[1]

# Instructions Productions


import ply.yacc as yacc
parser = yacc.yacc()

input = ''
s = ''
with open('./Proyecto1_G3/ArchivosPrueba/archivo.txt', 'r') as f:
    content = f.readlines()
    for element in content:
        s += element

input = s
print("El input es: [" + input + "]")

instrucciones = parser.parse(input)

for instruccion in instrucciones:
    print(instruccion) 




