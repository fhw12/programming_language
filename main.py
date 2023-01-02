import lexer
import ast

source = """

print(2 + 2 * 2)
print(5)
print(1)
"""

tokens = lexer.Lexer(source).parse()
root_node = ast.Ast(tokens).parse()

for token in tokens:
	print(token)

def print_node(node, i, text):
	if node.type == 'BinOp':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
		print_node(node.right, i+1, 'right')
	elif node.type == 'UnaryOp':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
	elif node.type == 'Compound':
		print(i * '\t' + f'{text}: Compound')
		print_node(node.left, i+1, 'left')
		print_node(node.right, i+1, 'right')
	elif node.type == 'Function':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
	elif node.type == 'Number':
		print(i * '\t' + f'{text}: {node.value}')

def calculator(node):
	if node.type == 'BinOp':
		if node.value == '+':
			result = calculator(node.left) + calculator(node.right)
		elif node.value == '-':
			result = calculator(node.left) - calculator(node.right)
		elif node.value == '*':
			result = calculator(node.left) * calculator(node.right)
		elif node.value == '/':
			result = calculator(node.left) / calculator(node.right)
		elif node.value == 'AND':
			result = calculator(node.left) and calculator(node.right)
		elif node.value == 'OR':
			result = calculator(node.left) or calculator(node.right)
		elif node.value == '<':
			result = calculator(node.left) < calculator(node.right)
		elif node.value == '>':
			result = calculator(node.left) > calculator(node.right)
		elif node.value == '<=':
			result = calculator(node.left) <= calculator(node.right)
		elif node.value == '>=':
			result = calculator(node.left) >= calculator(node.right)
		elif node.value == '==':
			result = calculator(node.left) == calculator(node.right)
		elif node.value == '!=':
			result = calculator(node.left) != calculator(node.right)
		return result
	elif node.type == 'UnaryOp':
		if node.value == '-':
			return -calculator(node.left)
	elif node.type == 'Number':
		return int(node.value)

print_node(root_node, 0, 'root')
#print(calculator(root_node))