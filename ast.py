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

	def parse(self):
		pass