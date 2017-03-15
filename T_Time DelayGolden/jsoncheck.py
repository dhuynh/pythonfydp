import json

with open("time_delay_inputs2.json") as f:
	raw_data = f.read()


time_delay_inputs = json.loads(raw_data)

print time_delay_inputs.keys()