import lexer

tokens = lexer.Lexer("10 + 2 * 2").parse()

for token in tokens:
	print(token)