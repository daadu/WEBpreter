import re
import ply.lex as lex

tokens = (
	"IDENTIFIER",
	"NUMBER",
	)
t_ignore = " "
def t_NUMBER(token):
	r"-?[0-9]+\.?[0-9]*"
	token.value = float(token.value)
	return token
def t_IDENTIFIER(token):
	r'[a-zA-Z]+_*'
	token.value = float(token.value)
	return token

script = "3.1 -1.2 -1. 3.4.5."
JavaScriptLexer = lex.lex()
JavaScriptLexer.input(script)
print script

while  True:
	tok = JavaScriptLexer.token()
	if not tok: break
	print tok