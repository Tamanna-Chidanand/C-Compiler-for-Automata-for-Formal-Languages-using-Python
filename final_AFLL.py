from turtle import fd
import ply.lex as lex
import ply.yacc as yacc

# Define the lexer tokens
tokens = (
    'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'LSQUARE', 'RSQUARE',
    'DO', 'WHILE', 'LPAREN', 'RPAREN', 'LBRAC', 'RBRAC', 'TYPE', 'ID',
    'SEMICOLON', 'COMMA', 'FOR', 'EQUAL', 'GREATER', 'LESSER', 'INC',
    'DEC', 'NUM', 'STAR',
)

# Regular expressions for tokens
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_DO = r'do'
t_WHILE = r'while'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRAC = r'\{'
t_RBRAC = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_FOR = r'for'
t_EQUAL = r'='
t_GREATER = r'>'
t_LESSER = r'<'
t_INC = r'\+\+'
t_DEC = r'--'
t_NUM = r'[0-9]+'
t_STAR = r'\*'

# Regular expression for 'ID' - exclude reserved keywords
reserved_keywords = {
    'int': 'TYPE',
    'float': 'TYPE',
    'double': 'TYPE',
    'char': 'TYPE',
    'for': 'FOR'
}

def t_TYPE(t):
    r'int|float|double|char'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved_keywords.get(t.value, 'ID')
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Ignore whitespace
t_ignore = ' \t'

# Define the grammar for BRACKET MATCHING
def p_brackets(p):
    '''
    s : LBRACE s RBRACE
             | LBRACE RBRACE
             | LBRACKET s RBRACKET
             | LBRACKET RBRACKET
             | LSQUARE s RSQUARE
             | LSQUARE RSQUARE
             | s s
    '''
    pass

# DEFINING THE GRAMMAR FOR DO-WHILE
def p_statement_do_while(p):
    'statement : DO LBRAC while_expression RBRAC WHILE LPAREN condition RPAREN'

def p_while_expression(p):
    'while_expression :'
    pass

def p_condition(p):
    'condition :'
    pass

# DEFINING GRAMMAR FOR FOR LOOP
def p_for(p):
    '''
    for : FOR LPAREN declaration SEMICOLON condition SEMICOLON increment RPAREN LBRACE ID RBRACE
    declaration : TYPE b SEMICOLON
    b :       ID
             | ID COMMA b
    condition : ID GREATER NUM
              | ID LESSER NUM
    increment : ID INC SEMICOLON
              | ID DEC SEMICOLON
'''

# GRAMMAR FOR VARIABLE DECLARATION
def p_declaration(p):
    '''
    declaration : TYPE a SEMICOLON
    a : ID
             | ID COMMA a
    '''

# GRAMMAR FOR FUNC DECLARATION
def p_function_declaration(p):
    '''
    function_declaration : TYPE ID LPAREN parameter_list RPAREN SEMICOLON
                        | TYPE ID LPAREN parameter_list RPAREN
                        | TYPE STAR ID LPAREN parameter_list RPAREN SEMICOLON
                        | TYPE STAR ID LPAREN parameter_list RPAREN
    '''

def p_parameter_list(p):
    '''
    parameter_list : TYPE ID
                  | parameter_list COMMA TYPE ID
                  | TYPE STAR ID
                  | parameter_list COMMA TYPE STAR ID
    '''

def p_error(p):
    print("Syntax error")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test C code with bracket matching
c_code = input("Enter:\n")

lexer.input(c_code)
for tok in lexer:
    print(tok)

result = parser.parse(c_code)

