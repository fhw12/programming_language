import lexer

source = """

(2 + 2) && 2

"""

tokens = lexer.Lexer(source).parse()

for token in tokens:
	print(token)