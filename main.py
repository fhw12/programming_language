import lexer
import ast

source = """

2 + 2 * 2

"""

tokens = lexer.Lexer(source).parse()
root_node = ast.Ast(tokens).PLUS_MINUS()

def print_node(node, i, text):
	node_type = node.type
	if node_type == 'BinOp':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
		print_node(node.right, i+1, 'right')
	elif node_type == 'Number':
		print(i * '\t' + f'{text}: {node.value}')

print_node(root_node, 0, 'root')