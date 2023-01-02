import lexer
import ast
import interpreter

source = """

a = 10

if(a != 10 && a > 3){
	print("a != 10 && a > 3")
}

if(a <= 12){
	if(a == 10){
		print("a == 10")
	}
	print("a <= 12")
}

if(a > 12){
	print("a > 12")
}

"""

tokens = lexer.Lexer(source).parse()

for token in tokens:
	print(token)

root_node = ast.Ast(tokens).parse()

def print_node(node, i, text):
	if node == None:
		return

	if node.type == 'BinOp':
		print(i * '\t' + f'{text}: {node.value}')
		print_node(node.left, i+1, 'left')
		print_node(node.right, i+1, 'right')
	elif node.type == 'Condition':
		print(i * '\t' + f'{text}: ')
		print_node(node.condition, i+1, 'condition')
		print_node(node.left, i+1, 'left')
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
	elif node.type == 'String':
		print(i * '\t' + f'{text}: {node.value}')
	elif node.type == 'Variable':
		print(i * '\t' + f'{text}: Variable')
		print_node(node.left, i+1, 'left')

print_node(root_node, 0, 'root')

interpreter.Interpreter().run(root_node)
