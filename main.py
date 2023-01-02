import lexer
import ast

source = """

(2 + 2) && 2

"""

tokens = lexer.Lexer(source).parse()
node = ast.Ast(tokens).parse()

for token in tokens:
	print(token)