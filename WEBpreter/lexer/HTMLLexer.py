import re
import ply.lex as lex

tokens = (		
		'LANGLE',
		'LANGLESLASH',
		'RANGLE',
		'EQUAL',#= 
		'STRING',#"anything"
		'WORD',#anything 
		)
states = (
	('htmlcomment','exclusive'),
	)

def t_htmlcomment(token):
	r"<!--"
	token.lexer.begin("htmlcomment")
def t_htmlcomment_end(token):
	r"-->"
	token.lexer.lineno += token.value.count("\n")
	token.lexer.begin("INITIAL")
def t_htmlcomment_error(token):
	token.lexer.skip(1)

t_ignore = " " #whitespace
def t_newline(token):
	r"\n"
	token.lexer.lineno += 1
	#token.lexer.colunmno = 0
	pass

def t_LANGLESLASH(token):
	r"</"
	return token
def t_LANGLE(token):
	r"<"
	return token
def t_RANGLE(token):
	r">"
	return token
def t_EQUAL(token):
	r"="
	return token
def t_STRING(token):
	r'"[^"]*"'
	token.value = token.value[1:-1]
	return token
def t_WORD(token):
	r'[^ <>\n]+'
	return token
#def t_NUMBER(token):
#	r"[0-9]+"
#	token.value = int(token.value)
#	return token

webpage = """This<!--comment 

sdhsdgfh


sdgfhjsgfhjdgfs<b>bold</b>--> is my <b>webpage !!!</b>
... COOl"""
HTMLlexer = lex.lex();
HTMLlexer.input(webpage)
print webpage
while True:
	tok = HTMLlexer.token()
	if not tok: break
	print tok