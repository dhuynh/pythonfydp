
import ast

solution = {}
raw_scanner_data = {}
transform_solution = {}

with open("solution.txt") as f:
	solution = f.read()

solution = ast.literal_eval(solution)

#print solution.keys()

stripped_key = ''

for combination in solution:
	raw_scanner_data = solution[combination]['scanner']
	for port in raw_scanner_data:
		stripped_key = port[8:]
		transform_solution[stripped_key] = raw_scanner_data[port]

print transform_solution

