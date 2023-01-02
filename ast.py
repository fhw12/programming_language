class Number():
	def __init__(self, value):
		self.type = 'Number'
		self.value = value

class BinOp():
	def __init__(self, value, right, left):
		self.type = 'BinOp'
		self.value = value
		self.right = right
		self.left = left

class Ast():
	def __init__(self, tokens):
		self.tokens = tokens
		self.pos = 0

	def get_current_token(self):
		return self.tokens[self.pos]

	def validation(self, token_type):
		token = self.get_current_token()
		if token.type != token_type:
			print(f"ERROR type ( {token_type} ) => {token}")
		self.pos += 1

	def NUMBER(self):
		token = self.get_current_token()
		if token.type == 'NUMBER':
			self.validation('NUMBER')
			node = Number(value=token.value)
		if token.type == 'LPARENT':
			self.validation('LPARENT')
			node = self.CALC()
			self.validation('RPARENT')
		return node

	def MUL_DIV(self):
		node = self.NUMBER()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type == 'MUL':
				self.validation('MUL')
				node = BinOp(value="*", left=node, right=self.NUMBER())
			elif token.type == 'DIV':
				self.validation('DIV')
				node = BinOp(value="/", left=node, right=self.NUMBER())
			else:
				return node
		return node

	def PLUS_MINUS(self):
		node = self.MUL_DIV()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type == 'PLUS':
				self.validation('PLUS')
				node = BinOp(value="+", left=node, right=self.MUL_DIV())
			elif token.type == 'MINUS':
				self.validation('MINUS')
				node = BinOp(value="-", left=node, right=self.MUL_DIV())
			else:
				return node
		return node

	def AND(self):
		node = self.PLUS_MINUS()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type == 'AND':
				self.validation('AND')
				node = BinOp(value="AND", left=node, right=self.PLUS_MINUS())
			else:
				return node
		return node

	def OR(self):
		node = self.AND()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type == 'OR':
				self.validation('OR')
				node = BinOp(value="OR", left=node, right=self.AND())
			else:
				return node
		return node

	def CALC(self):
		node = self.OR()
		return node

	def parse(self):
		pass