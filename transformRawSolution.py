
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
	port_dict_scanner = {}
	for port in raw_scanner_data:
		stripped_key = port[8:]
		stripped_key = stripped_key[1:-1]
		port_dict_scanner[stripped_key] = raw_scanner_data[port]
	transform_solution[combination] = port_dict_scanner

print transform_solution

