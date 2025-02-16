import math
import operator
import ast

import sympy as sp

def safe_eval(expression):
    allowed_functions = {
        "sqrt": math.sqrt, "pow": math.pow, "abs": abs, "round": round,
        "log": math.log, "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "pi": math.pi, "e": math.e, "factorial": math.factorial,
        "perm": math.perm, "comb": math.comb, "det": np.linalg.det,
        "inv": np.linalg.inv, "matrix": np.array, "diff": sp.diff, "integrate": sp.integrate,
        "complex": complex
    }
    try:
        node = ast.parse(expression, mode='eval')
        if not all(isinstance(n, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Call, ast.Load, ast.Name)) for n in ast.walk(node)):
            raise ValueError("Invalid expression")
        return eval(expression, {"__builtins__": None}, allowed_functions)
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Advanced Scientific Calculator")
    print("Supports: Basic math, trig, log, factorial, matrices, calculus, and complex numbers.")
    print("Enter an expression to evaluate or type 'exit' to quit.")
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        print("Result:", safe_eval(expression))

if __name__ == "__main__":
    main()
