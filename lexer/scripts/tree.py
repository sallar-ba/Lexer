import ast

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_expression_tree(expression):
    tree = ast.parse(expression, mode='eval')

    def build_tree(node):
        if isinstance(node, ast.BinOp):
            return Node(ast.get_source_segment(expression, node),
                        build_tree(node.left),
                        build_tree(node.right))
        else:
            return Node(ast.get_source_segment(expression, node))

    return build_tree(tree.body)

def print_tree(node, indent=''):
    if node is None:
        return

    print(indent + '└── ' + str(node.value))
    
    if node.left is not None:
        print_tree(node.left, indent + '    │')
    
    if node.right is not None:
        print_tree(node.right, indent + '     ')

