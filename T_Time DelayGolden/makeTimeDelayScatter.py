import json
import csv

with open("time_delay_output.json") as f:
	raw_data = f.read()


time_delay_output = json.loads(raw_data)

new_output = []

for combination in time_delay_output:
	for port in time_delay_output[combination]:
		new_output.append((combination, time_delay_output[combination][port]))



with open("time_delay_output.csv", 'wb') as s:
	csvwrite = csv.writer(s)

	for points in new_output:
		csvwrite.writerow(points)