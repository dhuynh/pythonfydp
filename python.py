
import ast

solution = {}
transformsolution = []

with open("solution.txt") as f:
	solution = f.read()

solution = ast.literal_eval(solution)

print solution.keys()

