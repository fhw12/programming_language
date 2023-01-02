class Interpreter():
	def __init__(self):
		pass

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
			return result
		elif node.type == 'UnaryOp':
			if node.value == '-':
				return -run(node.left)
		elif node.type == 'Compound':
			self.run(node.left)
			self.run(node.right)
		elif node.type == 'Function':
			if node.value == 'PRINT':
				print(self.run(node.left))
		elif node.type == 'Number':
			return int(node.value)