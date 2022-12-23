'''
Grupo 3 :^)
'''

import sys
import os
import re 
reserved = {
    'print' :   'RPRINT',    
    # Comienzan Tipos Basico
    'None'  :   'RNONE',
    'int'   :   'RINT',
    'float' :   'RFLOAT',
    'bool'  :   'RBOOL',
    'string':   'RSTRING',
    'false' :   'RFALSE',
    'true'  :   'RTRUE',
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
    "CADENA",
    'ID',
    ### arithmetics tokens     
    'EQUALS',
    'PLUS',
    'MINUS',
    'POR',
    'DIVIDE',
    'MODULATE',
    'POT',
    ### arithmetics tokens type date
    'FLOAT',
    'INTEGER'
    
    

] + list(reserved.values())

# Tokens Definitions
t_SALTOLINEA = r'\n'
t_DOSPUNTOS = r';'
t_PARIZQ = r'\('
t_PARDER = r'\)'
### arithmetics tokens init 
t_EQUALS    = r'\='
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_POR       = r'\*'
t_DIVIDE    = r'\/'
t_MODULATE  = r'\%'
t_POT      = r'\*\*'

# Comment multiline
def t_COMMENUNI(t):
    r'\#\=(.|\n)*?\=\#'
    t.lexer.lineno += t.value.count('\n')
    # print('Token multilinea')

# Comment unline
def t_COMMENMUL(t):
    r'\#.*\n'
    t.lexer.lineno += 1
    # print('Token unilinea')

### methods for tokens INTEGER , DECIMAL  
def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("FLOAT VALUE ERROR TO LARGE %d",t.value)
        t.value = 0
    return t

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("INTEGER VALUE ERROR %d",t.value)
        t.value = 0
    return t


### end methods for arithmetics 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # revisar en la lista de reservadas
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


### end lexical format
### init imports grammar
from expressions.expressions import *
from instruction.asignacion import Asignacion
### end imports grammar 
# Grammar definition
### precedence

### end precedence 



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
    '''
    t[0] = t[1]

def p_finins(t):
    '''finins       : SALTOLINEA
                    | '''
    t[0] = None

# Error Production (Semantic)
def p_instruccion_error(t):
    'instruccion  : error finins'
    print("ERROR - ", "Error Sintáctico. Instruccion " + str(t[1].value), t.lineno(1), find_column(input, t.slice[1]))
    t[0] = ""

# Expressions Options

def p_print_instr(t):
    'print_instr  : RPRINT PARIZQ expresion PARDER'
    t[0] = "Print Reconocido - " + str(t[3])

def p_expresion_cadena(t):
    'expresion  : CADENA'
    t[0] = "Cadena Reconocida: " + t[1]

def p_expresion_id(t):
    'expresion  :   ID'
    t[0] = "ID Reconocido: " + t[1]

# Instructions Productions
### declaration options 

def p_asignacion_instr(t):
    'asignacion_instr  : ID EQUALS expresion' 
    t[0] = Asignacion(t[1],t[3])
### end declaration options 
### Arithmetic Options 
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




def p_expresion_agrupacion(t):
    'expresion  :   PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''
    expresion   :   INTEGER
                |   FLOAT
    '''
    t[0] = t[1]


### END Arithmetic Options


### LOGIC expression grammar 

### end logic expresion grammar 

import ply.yacc as yacc
parser = yacc.yacc()

input = ''
s = ''
with open('Proyecto1_G3/ArchivosPrueba/archivo.txt', 'r') as f:
    content = f.readlines()
    for element in content:
        s += element

input = s
print("\n\nEl input es: [\n" + input + "\n]\n\n")

instrucciones = parser.parse(input)

for instruccion in instrucciones:
    if instruccion == None:
        print("Error En Gramatica xd")
    else:
        print(instruccion) 




