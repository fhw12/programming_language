import lexer
import ast

source = """

2 + 2 * 2 == 6

"""

tokens = lexer.Lexer(source).parse()
root_node = ast.Ast(tokens).CALC()

for token in tokens:
	print(token)

def print_node(node, i, text):
	if node.type == 'BinOp':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
		print_node(node.right, i+1, 'right')
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
	elif node.type == 'Number':
		return int(node.value)

print_node(root_node, 0, 'root')
print(calculator(root_node))