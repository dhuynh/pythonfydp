#!/usr/bin/python

import json
import ast

solution = {}
raw_scanner_data = {}
transform_solution = {}

#Data Variables
scannerFreqDict = {}

def clearScannerNames(solution):
	for combination in solution:
		raw_scanner_data = solution[combination]['vars']
		port_dict_scanner = {}
		for port in raw_scanner_data:
			stripped_key = port[1:]
			stripped_key = stripped_key[1:-1]
			port_dict_scanner[stripped_key] = raw_scanner_data[port]
		solution[combination]['scanner'] = port_dict_scanner
	return

def findScannerFrequency(solution):
	for combination in solution:
		for port in solution[combination]['vars']:
			if solution[combination]['vars'][port] == 1:
				try:
					scannerFreqDict[port] +=1
				except KeyError:
					scannerFreqDict[port] = 1

	return


#mainRun


with open("solution.txt") as f:
	solution = f.read()

solution = ast.literal_eval(solution)

#print solution.keys()
stripped_key = ''

#clearScannerNames(solution)

#findScannerFrequency(solution)

#print scannerFreqDict

with open('transformed.json', 'w') as solution_dump:
	json.dump(solution, solution_dump, sort_keys=True)

with open('scannerFreq.json', 'w') as scannerFreqDump:
	json.dump(scannerFreqDict, scannerFreqDump, sort_keys=True)



