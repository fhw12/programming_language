class Token():
	def __init__(self, token_type, token_value):
		self.type = token_type
		self.token_value = token_value

class Lexer():
	def __init__(self, source):
		self.source = source
		self.pos = 0