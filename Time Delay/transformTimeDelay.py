#!/usr/bin/python

from pdb import set_trace as bp

import json
import ast

raw_verbose_data = {}

#Track if Port has been counted, record TEU
scanner_port_filled_dict = {}

'''transform to json
#or combination in raw_data
raw_verbose_data = raw_data[combination]['scanner']
for each scanner port, calculate total TEU
store TEU arriving
Find scanning capacity after'''

def findScannersAndContainerCount(raw_data):
	stripped_key = ''
	scanner = ''
	for combination in raw_data:
		raw_verbose_data = raw_data[combination]['scanner']
		scanner_port_filled_dict[combination] = {}
		for foreign_or_dest_or_scanner in raw_verbose_data:
			print foreign_or_dest_or_scanner
			if foreign_or_dest_or_scanner[:12] == 'foreign_ship':
				stripped_key = foreign_or_dest_or_scanner[12:]
				stripped_key = stripped_key[1:-1]
				scanner_port = stripped_key.split(",", 1)[-1]

				if raw_verbose_data[foreign_or_dest_or_scanner] != 0.0:
					if not existInDict(scanner_port, scanner_port_filled_dict[combination]):
						scanner_port_filled_dict[combination][scanner_port] = {}
						scanner_port_filled_dict[combination][scanner_port]['Total_TEU'] = 0
					try:
						scanner_port_filled_dict[combination][scanner_port]['Total_TEU'] += raw_verbose_data[foreign_or_dest_or_scanner]
					except KeyError:
						scanner_port_filled_dict[combination][scanner_port]['Total_TEU'] = raw_verbose_data[foreign_or_dest_or_scanner]
			elif foreign_or_dest_or_scanner[:8] == 'scanners':
				stripped_key = foreign_or_dest_or_scanner[8:]
				scanner_port = stripped_key[1:-1]
				bp()


				if not existInDict(scanner_port, scanner_port_filled_dict[combination]):
						scanner_port_filled_dict[combination][scanner_port] = {}
						scanner_port_filled_dict[combination][scanner_port]['scanners'] = 0

				if raw_verbose_data[foreign_or_dest_or_scanner] is not None:
					scanner_port_filled_dict[combination][scanner_port]['scanners'] = raw_verbose_data[foreign_or_dest_or_scanner]
			elif foreign_or_dest_or_scanner[:9] == 'dest_ship':
				pass
	print scanner_port_filled_dict
	return

def existInDict(scanner_port, port_dict):
	for key in port_dict:
		if scanner_port == key:
			return True
		else:
			return False







#mainRun


with open("verbose_result.txt") as f:
	raw_data = f.read()

raw_data = ast.literal_eval(raw_data)

#print solution.keys()


findScannersAndContainerCount(raw_data)


#with open('scannerData.json', 'w') as solution_dump:
#	json.dump(solution, solution_dump, sort_keys=True)

#with open('scannerFreq.json', 'w') as scannerFreqDump:
#	json.dump(scannerFreqDict, scannerFreqDump, sort_keys=True)



