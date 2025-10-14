# This is a basic 4-function calculator that shows ASCII UI, takes an expression,
# and evaluates it safely (no eval) using Python's AST.

import ast, operator

print("\nWelcome to Nevaeh's 4-function calculator!")
print("""
 ________________________________
|   __________________________   |
|  |         Calculator       |  |
|  |__________________________|  |
|   _____ _____ _____    _____   |
|  |  7  |  8  |  9  |  |  +  |  |
|  |_____|_____|_____|  |_____|  |
|  |  4  |  5  |  6  |  |  -  |  |
|  |_____|_____|_____|  |_____|  |
|  |  1  |  2  |  3  |  |  x  |  |
|  |_____|_____|_____|  |_____|  |
|  |  .  |  0  |  =  |  |  /  |  |
|  |_____|_____|_____|  |_____|  |
|                                |
|________________________________|
""")

def calculate(expr: str) -> float:
	# Let users type 'x' or 'X' for multiply
	expr = expr.replace('x', '*').replace('X', '*')

	# Map AST operator nodes to real functions
	ops = {
			ast.Add:  operator.add,      # +
			ast.Sub:  operator.sub,      # -
			ast.Mult: operator.mul,      # *
			ast.Div:  operator.truediv,  # /
			ast.USub: operator.neg,      # unary minus: -a
			ast.UAdd: operator.pos       # unary plus: +a (optional)
	}

	def eval_node(node):
		# Root wrapper for an expression like "8+9*(9/3)"
		if isinstance(node, ast.Expression):
			return eval_node(node.body)

		# Binary operation: a OP b (e.g., 3 + 4, 8 * 2)
		if isinstance(node, ast.BinOp):
			left = eval_node(node.left)
			right = eval_node(node.right)
			op_fn = ops.get(type(node.op))
			if not op_fn:
					raise ValueError("Operator not allowed.")
			return op_fn(left, right)

		# Unary operation: -a or +a
		if isinstance(node, ast.UnaryOp):
			op_fn = ops.get(type(node.op))
			if not op_fn:
					raise ValueError("Operator not allowed.")
			return op_fn(eval_node(node.operand))

		# Numeric literal (int or float)
		if isinstance(node, ast.Constant):
			if isinstance(node.value, (int, float)):
					return float(node.value)
			raise ValueError("Only numbers are allowed.")

		# (Older Python) numeric nodes
		if hasattr(ast, "Num") and isinstance(node, ast.Num):
			return float(node.n)

		# Anything else (names, calls, etc.) is blocked
		raise ValueError("Unsupported input.")

	# Parse safely into an AST and evaluate
	tree = ast.parse(expr, mode="eval")
	return eval_node(tree)

# Run once
equation = input("Enter your equation: ")
try:
    print("= ", calculate(equation))
except ZeroDivisionError:
    print("Error: division by zero.")
except Exception as e:
    print("Error:", e)
