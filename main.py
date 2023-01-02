import lexer
import ast
import interpreter

source = """
print(1)
print(2)
print(1 + 2)
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

print_node(root_node, 0, 'root')

interpreter.Interpreter().run(root_node)
