class Number():
	def __init__(self, value):
		self.type = 'Number'
		self.value = value

class String():
	def __init__(self, value):
		self.type = 'String'
		self.value = value

class BinOp():
	def __init__(self, value, left, right):
		self.type = 'BinOp'
		self.value = value
		self.right = right
		self.left = left

class UnaryOp():
	def __init__(self, value, left):
		self.type = 'UnaryOp'
		self.value = value
		self.left = left

class Compound():
	def __init__(self, left, right):
		self.type = 'Compound'
		self.left = left
		self.right = right

class Function():
	def __init__(self, value, left):
		self.type = 'Function'
		self.value = value
		self.left = left

class Variable():
	def __init__(self, name, left):
		self.type = 'Variable'
		self.name = name
		self.left = left

class Condition():
	def __init__(self, condition, left, right):
		self.type = 'Condition'
		self.condition = condition
		self.left = left
		self.right = right

class Loop():
	def __init__(self, condition, left):
		self.type = 'Loop'
		self.condition = condition
		self.left = left

class NullNode():
	def __init__(self):
		self.type = 'NullNode'

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
		elif token.type == 'LPARENT':
			self.validation('LPARENT')
			node = self.CALC()
			self.validation('RPARENT')
		elif token.type == 'MINUS':
			self.validation('MINUS')
			node = UnaryOp(value="-", left=self.NUMBER())
		elif token.type == 'ID':
			self.validation('ID')
			node = Variable(name=token.value, left=None)
		elif token.type == 'STRING':
			self.validation('STRING')
			node = String(value=token.value)
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
			elif token.type == '..':
				self.validation('..')
				node = BinOp(value="..", left=node, right=self.MUL_DIV())
			else:
				return node
		return node

	def CMP(self):
		node = self.PLUS_MINUS()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type in ['<', '>', '<=', '>=', '!=', '==']:
				self.validation(token.type)
				node = BinOp(value=token.type, left=node, right=self.PLUS_MINUS())
			else:
				return node
		return node

	def AND(self):
		node = self.CMP()
		while self.pos < len(self.tokens):
			token = self.get_current_token()

			if token.type == 'AND':
				self.validation('AND')
				node = BinOp(value='AND', left=node, right=self.CMP())
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
		node = NullNode()
		while self.pos < len(self.tokens):
			token = self.get_current_token()
			
			if token.type == 'PRINT':
				self.validation('PRINT')
				self.validation('LPARENT')
				node = Compound(left=node, right=Function(left=self.CALC(), value='PRINT'))
				self.validation('RPARENT')
			elif token.type == 'ID':
				self.validation('ID')
				self.validation('ASSIGN')
				node = Compound(left=node, right=Variable(name=token.value, left=self.CALC()))
			elif token.type == 'IF':
				self.validation('IF')
				self.validation('LPARENT')
				condition = self.CALC()
				self.validation('RPARENT')
				self.validation('LBLOCK')
				left = self.parse()
				#node = Compound(left=node, right=Condition(condition=condition, left=self.parse()))
				self.validation('RBLOCK')

				right = NullNode()
				if self.get_current_token().type == 'ELSE':
					self.validation('ELSE')
					self.validation('LBLOCK')
					right = self.parse()
					self.validation('RBLOCK')
				node = Compound(left=node, right=Condition(condition=condition, left=left, right=right))

			elif token.type == 'WHILE':
				self.validation('WHILE')
				self.validation('LPARENT')
				condition = self.CALC()
				self.validation('RPARENT')
				self.validation('LBLOCK')
				node = Compound(left=node, right=Loop(condition=condition, left=self.parse()))
				self.validation('RBLOCK')
			else:
				return node
		return node