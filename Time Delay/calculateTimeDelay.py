
import json

#work on time delay input equation

'''y = 1/(c*mu*(1-lambda/(c*mu))) + 1/mu;

c is the number of scanners, lambda is the number of containers arriving per x amount of time

mu is scanning capacity per x amount of time

(mu is 10 per hour, can be multiplied to get days or years)'''

raw_data = {}
time_delay_output = {}

def calculateFullSet(time_delay_inputs):
	for combination in time_delay_inputs:
		for port in time_delay_inputs[combination]:
			h = float(time_delay_inputs[combination][port]['Total_TEU'])
			c = float(time_delay_inputs[combination][port]['scanners'])
			time_delay_output[port] = timeDelayEquation(h, c)
	return

def timeDelayEquation(h, c):
	mu = float(10*24*365)
	timeDelay = float(1/(c*mu*((1-h)/(c*mu))) + 1/mu)
	return timeDelay





with open("time_delay_inputs.json") as f:
	raw_data = f.read()


time_delay_inputs = json.loads(raw_data)

calculateFullSet(time_delay_inputs)

with open("time_delay_output.json", 'w') as s:
	json.dump(time_delay_output, s, sort_keys=True)

