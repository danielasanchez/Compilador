import ply.lex as lex


#establecen el codigo que se desea analizar
program = '''
    
#este es un comentario
CONST edad=18
VAR meses=edad*12
VAR residuo=5%2

IF edad>=18
 PRINT("Eres mayor de edad")
ELSE
 PRINT("Eres menor de edad")
END


'''

reservadas = ['BEGIN',
              'END',
              'IF',
              'THEN',
              'WHILE',
              'DO',
              'CALL',
              'CONST',
              'VAR',
              'PROCEDURE',
              'OUT',
              'IN',
              'ELSE',
              'PRINT']

tokens = ['ID',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'ODD',
          'ASSIGN',
          'NE',
          'LT',
          'LTE',
          'GT',
          'GTE',
          'LPARENT', 
          'RPARENT',
          'COMMA',
          'SEMMICOLOM',
          'DOT',
          'UPDATE',
          'QUOTES',
          'MOD'
          ]

tokens = tokens+reservadas

#se agrega en PALABRA a tokens y a continuacion se establece
#el simbolo utilizado iniciando con t_PALABRA
t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='
t_QUOTES = r'\"' 
t_MOD = r'\%'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value in reservadas:
		#t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    #para comentarios con #
    r'\#.*'
    #para comentarios con //
    #r'\//.*'
    pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)



analizador = lex.lex()

analizador.input(program)

while True:
	tok = analizador.token()
	if not tok : break
	print(tok)



	
