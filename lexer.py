class Token():
	def __init__(self, token_type, token_value):
		self.type = token_type
		self.value = token_value
	def __str__(self):
		return f'Token("{self.type}", "{self.value}")'

class Lexer():
	def __init__(self, source):
		self.source = source
		self.tokens = []
		self.pos = 0

	def add_token(self, token_type, token_value):
		self.tokens.append(Token(token_type, token_value))

	def get_current_char(self):
		return self.source[self.pos]

	def get_next_char(self):
		if self.pos + 1 < len(self.source):
			return self.source[self.pos + 1]
		else:
			return ''

	def parse_number(self):
		result = ""

		while self.pos < len(self.source) and self.get_current_char().isdigit():
			char = self.get_current_char()
			result += char
			self.pos += 1
		self.pos -= 1

		return result

	def parse(self):
		while self.pos < len(self.source):
			char = self.get_current_char()
			next_char = self.get_next_char()

			if char + next_char == '&&':
				self.add_token('AND', '&&')
				self.pos += 1
			elif char + next_char == '||':
				self.add_token('OR', '||')
				self.pos += 1
			elif char + next_char == '<=':
				self.add_token('<=', '<=')
				self.pos += 1
			elif char + next_char == '>=':
				self.add_token('>=', '>=')
				self.pos += 1
			elif char + next_char == '==':
				self.add_token('==', '==')
				self.pos += 1
			elif char + next_char == '!=':
				self.add_token('!=', '!=')
				self.pos += 1
			elif char == '<':
				self.add_token('<', char)
			elif char == '>':
				self.add_token('>', char)
			elif char.isdigit():
				self.add_token('NUMBER', self.parse_number())
			elif char == '+':
				self.add_token('PLUS', char)
			elif char == '-':
				self.add_token('MINUS', char)
			elif char == '*':
				self.add_token('MUL', char)
			elif char == '/':
				self.add_token('DIV', char)
			elif char == '(':
				self.add_token('LPARENT', char)
			elif char == ')':
				self.add_token('RPARENT', char)

			self.pos += 1

		return self.tokens