class Interpreter():
	def __init__(self):
		self.variables = {}

	def run(self, node):
		if node.type == 'BinOp':
			if node.value == '+':
				result = self.run(node.left) + self.run(node.right)
			elif node.value == '-':
				result = self.run(node.left) - self.run(node.right)
			elif node.value == '*':
				result = self.run(node.left) * self.run(node.right)
			elif node.value == '/':
				result = self.run(node.left) / self.run(node.right)
			elif node.value == 'AND':
				result = self.run(node.left) and self.run(node.right)
			elif node.value == 'OR':
				result = self.run(node.left) or self.run(node.right)
			elif node.value == '<':
				result = self.run(node.left) < self.run(node.right)
			elif node.value == '>':
				result = self.run(node.left) > self.run(node.right)
			elif node.value == '<=':
				result = self.run(node.left) <= self.run(node.right)
			elif node.value == '>=':
				result = self.run(node.left) >= self.run(node.right)
			elif node.value == '==':
				result = self.run(node.left) == self.run(node.right)
			elif node.value == '!=':
				result = self.run(node.left) != self.run(node.right)
			elif node.value == '..':
				result = str(self.run(node.left)) + str(self.run(node.right))
			return result
		elif node.type == 'UnaryOp':
			if node.value == '-':
				return -self.run(node.left)
		elif node.type == 'Compound':
			self.run(node.left)
			self.run(node.right)
		elif node.type == 'Function':
			if node.value == 'PRINT':
				print(self.run(node.left))
			elif node.value == 'INPUT':
				self.variables[node.left.name] = input()
			elif node.value == 'INT':
				self.variables[node.left.name] = int(self.variables[node.left.name])
			elif node.value == 'STR':
				self.variables[node.left.name] = str(self.variables[node.left.name])
		elif node.type == 'Number':
			return int(node.value)
		elif node.type == 'String':
			return node.value
		elif node.type == 'Variable':
			if node.left != None:
				self.variables[node.name] = self.run(node.left)
			else:
				return self.variables[node.name]
		elif node.type == 'Condition':
			if self.run(node.condition):
				self.run(node.left)
			else:
				self.run(node.right)
		elif node.type == 'Loop':
			while self.run(node.condition):
				self.run(node.left)