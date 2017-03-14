import json
import ast

with open('portlatlong200gold.json') as datap:    
    data1 = json.load(datap)

with open('scannerFreqCopy.json') as dataq:    
    data2 = json.load(dataq)



for port in data2:
	for entry in data1:
		if port == entry['ID']:
			entry['Freq'] = data2[port]

with open('portlatlong200goldoutput.json', 'w') as data_output:    
    data_output = json.dump(data1, data_output)