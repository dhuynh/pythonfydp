
import json
import ast

pareto = []

def createPareto(solution):
	for scannerNum in solution:
		values = {}
		values['Transshipment'] = solution[scannerNum]['obj']
		values['Scanners'] = scannerNum
		pareto.append(values)


with open("solutiongold.txt") as f:
	solution = f.read()

solution = ast.literal_eval(solution)

createPareto(solution)


with open('pareto.json', 'w') as solution_dump:
	json.dump(pareto, solution_dump, sort_keys=True)