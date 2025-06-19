import ast
import operator as op
from typing import Union


def _eval(node: ast.AST) -> Union[int, float]:
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        ops = {
            ast.Add: op.add,
            ast.Sub: op.sub,
            ast.Mult: op.mul,
            ast.Div: op.truediv,
            ast.Pow: op.pow,
            ast.Mod: op.mod,
        }
        if type(node.op) not in ops:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        return ops[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        operand = _eval(node.operand)
        return +operand if isinstance(node.op, ast.UAdd) else -operand
    else:
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")


def calculate(expression: str) -> Union[int, float]:
    """Safely evaluate a simple arithmetic expression."""
    tree = ast.parse(expression, mode="eval")
    return _eval(tree.body)


if __name__ == "__main__":
    expr = input("Enter expression: ")
    try:
        result = calculate(expr)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
