# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 


reserved = {
    'INT' : 'type_int',
    'FLOAT' : 'type_float',
    'DOUBLE' : 'type_double',
    'CHAR' : 'type_char',
    'STRING' : 'type_string',
    'LONG' :'type_long',
    'CHAR' : 'type_char',
    'IF' : 'type_if',
    'ELSE' : 'type_else',
    'while' : 'type_WHILE',
    'and' : 'type_AND',
    'or' : 'type_OR',
    'not' : 'type_NOT',
    'true' : 'type_TRUE',
    'false' : 'type_FALSE',
    'void' : 'type_VOID',
    'RETURN' : 'type_RETURN',
    'print' : 'type_PRINT',
    'input' : 'type_INPUT',
    'len' : 'type_LEN',
    'range' : 'type_RANGE',
    'in' : 'type_IN',
    'for' : 'type_FOR',
    'break' : 'type_BREAK',
    'continue' : 'type_CONTINUE',
    'def' : 'type_DEF',
    'class' : 'type_CLASS',
    'import' : 'type_IMPORT',
    'from' : 'type_FROM',
    'DO' : 'type_do',
    'WHILE' : 'type_while',
    'BOOL' : 'type_bool',
    'COUT' : 'type_cout',
    'CIN' : 'type_cin',
    'finalFuncion' : 'type_FinalFuncion',
    'finalFor' : 'type_FinalFor',
    'REPLENISH' : 'type_REPLENISH',
    'finalWhile' : 'type_FinalWhile',
    'funPrincipal' : 'type_funPrincipal',
    'finalfuncionSec' : 'type_finalfuncionSec',
    'finalIf' : 'type_finalIf',
    'finalswitch' : 'type_finalswitch',
    'salirBucle' : 'type_salirBucle',
    'caseSwitch' : 'type_caseSwitch',
    'porDefecto' : 'type_porDefecto'
}

 # List of token names.   This is always required
tokens = [
    'num',
    'Suma',
    'Resta',
    'Mult',
    'Div',
    'parentesisIZQ',
    'parentesisDER',
    'Asignacion',
    'menor_que',
    'mayor_que',
    'igual_que',
    'diferente_que',
    'opuesto_que',
    'mayorIgual_que',
    'menorIgual_que',
    'corcheteIZQ',
    'corcheteDER',
    'llaveIZQ',
    'llaveDER',
    'CometariosLineal',
    'CometariosMultiple',
    'comillasdobles',
    'comillasSimples',
    'ID',
    'modulo',
    'SumaunoAuno',
    'decimal',
] + list(reserved.values())

 # Regular expression rules for simple tokens
t_Suma    = r'\+'
t_Resta   = r'-'
t_Mult   = r'\*'
t_Div  = r'/'
t_parentesisIZQ  = r'\('
t_parentesisDER  = r'\)'
t_Asignacion  = r'\='
t_menor_que  = r'\<'
t_mayor_que  = r'\>'
t_igual_que  = r'\='
t_diferente_que  = r'\!\='
t_opuesto_que  = r'\!' 
t_mayorIgual_que  = r'\<\='
t_menorIgual_que  = r'\>\='
t_corcheteIZQ  = r'\{'
t_corcheteDER  = r'\}'
t_llaveIZQ  = r'\['
t_llaveDER  = r'\]'
t_CometariosLineal = r'//.*'
t_CometariosMultiple = r'/\*(.|\n)*?\*/'
t_comillasdobles = r'\".*\"'
t_comillasSimples = r'\'.*?\''
t_modulo = r'%'
t_SumaunoAuno = r'\+\+'
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_decimal = r'[0-9]+\.[0-9]+'





#t_NUMBER  = r'\d+'

 # A regular expression rule with some action code

def t_num(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t

 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Give the lexer some input

def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        lexer.input(data)
        tokens_list = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_list.append({'type': tok.type, 'lexeme': tok.value, 'line': tok.lineno, 'column': tok.lexpos})
    return tokens_list

# Test de la función
if __name__ == '__main__':
    file_path = 'hola.txt'
    tokens = tokenize_file(file_path)
    for token in tokens:
        print(token)