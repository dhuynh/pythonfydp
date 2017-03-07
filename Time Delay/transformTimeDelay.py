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

			if foreign_or_dest_or_scanner[:12] == 'foreign_ship':
				stripped_key = foreign_or_dest_or_scanner[12:]
				stripped_key = stripped_key[1:-1]
				scanner_port = stripped_key.split(",", 1)[-1]

				if raw_verbose_data[foreign_or_dest_or_scanner] != 0.0:

					'''print "foreign -> " + scanner_port
					print "value -> " + str(raw_verbose_data[foreign_or_dest_or_scanner])

					bp()'''

					if not existInDict(scanner_port, scanner_port_filled_dict[combination]):
						populateScannerKeys(scanner_port, scanner_port_filled_dict[combination])

						'''print "Does not Exist so fill"
						print scanner_port_filled_dict
						bp()'''

					try:
						scanner_port_filled_dict[combination][scanner_port]['Total_TEU'] += round(raw_verbose_data[foreign_or_dest_or_scanner], 2)

						'''print "Add TEU"
						print scanner_port_filled_dict
						bp()'''

					except KeyError:
						scanner_port_filled_dict[combination][scanner_port]['Total_TEU'] = raw_verbose_data[foreign_or_dest_or_scanner]

						'''print "set TEU"
						print scanner_port_filled_dict
						bp()'''

			elif foreign_or_dest_or_scanner[:8] == 'scanners':


				stripped_key = foreign_or_dest_or_scanner[8:]
				scanner_port = stripped_key[1:-1]

				if raw_verbose_data[foreign_or_dest_or_scanner] != 0.0:

					'''print "scanners -> " + scanner_port
					print "value -> " + str(raw_verbose_data[foreign_or_dest_or_scanner])
					bp()'''

					if not existInDict(scanner_port, scanner_port_filled_dict[combination]):
						populateScannerKeys(scanner_port, scanner_port_filled_dict[combination])

						'''print "Does not Exist so fill"
						print scanner_port_filled_dict
						bp()'''
						
					scanner_port_filled_dict[combination][scanner_port]['scanners'] = round(raw_verbose_data[foreign_or_dest_or_scanner],1)

					'''print "Set Scanner"
					print scanner_port_filled_dict
					bp()'''

			elif foreign_or_dest_or_scanner[:9] == 'dest_ship':
				pass

	print scanner_port_filled_dict
	return

def existInDict(scanner_port, port_dict):
	for key in port_dict:
		if scanner_port == key:
			return True
	return False

def populateScannerKeys(scanner_port, port_dict):
	port_dict[scanner_port] = {}
	port_dict[scanner_port]['scanners'] = 0
	port_dict[scanner_port]['Total_TEU'] = 0



def existInDictScanner(scanner_port, port_dict):
	for key in port_dict:
		if scanner_port == key:
			return True
		else:
			return False



#mainRun


with open("verbose_result.txt") as f:
	raw_data = f.read()

raw_data = ast.literal_eval(raw_data)

findScannersAndContainerCount(raw_data)


#with open('scannerData.json', 'w') as solution_dump:
#	json.dump(solution, solution_dump, sort_keys=True)

with open('time_delay_inputs.json', 'w') as time_inputs:
	json.dump(scanner_port_filled_dict, time_inputs, sort_keys=True)



