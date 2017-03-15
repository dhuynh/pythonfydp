
import json
import math as m

#work on time delay input equation

'''y = 1/(c*mu*(1-lambda/(c*mu))) + 1/mu;

c is the number of scanners, lambda is the number of containers arriving per x amount of time

mu is scanning capacity per x amount of time

(mu is 10 per hour, can be multiplied to get days or years)'''

raw_data = {}
time_delay_output = {}

def calculateFullSet(time_delay_inputs):
	for combination in time_delay_inputs:
		time_delay_output[combination] = {}
		for port in time_delay_inputs[combination]:
			h = float(time_delay_inputs[combination][port]['Total_TEU'])
			c = float(time_delay_inputs[combination][port]['scanners'])
			if c and h !=0.0:
					time_delay_output[combination][port] = timeDelayEquation(h, c)

	return


def timeDelayEquation(h, c):
	mu = float(10*24*365*1.5001)

	p = h/(c*mu)


	pnot = 0
	pq = 0
	time_delay = 0

	pnot = calculatePnot(c,p)
	pq = calculatePq(c,p,pnot)
	time_delay = calculateTw(pq,p,h,mu)

	#print pnot, pq, time_delay

	return time_delay

def calculateTw(pq,p,h,mu):
	return (pq*(p/(h*(1-p))) + (1/mu))

def calculatePq(c,p,pnot):
	return (m.pow(c*p,c)/m.factorial(int(c))) * (1/(1-p)) * pnot


def calculatePnot(c,p):
	pnot = 0
	print 'p: ' + str(p), 'c: ' + str(c)
	print int(c-1) == 0
	for k in range(0,int(c-1)):
		print 'first term: ' + str(firstTerm(c,p,k)), 'second term: ' + str(secondTerm(c,p))
		pnot += firstTerm(c,p,k) + secondTerm(c,p)

	print type(c)
	print c == 1.0
	if int(c-1) == 0:
		print 'first term: ' + str(firstTerm(c,p,1)), 'second term: ' + str(secondTerm(c,p))
		pnot += firstTerm(c,p,1) + secondTerm(c,p)

	print 'pnot:' + str(pnot)

	pnot = 1/pnot

	return pnot

def firstTerm(c,p,k):
	return (m.pow(c*p,k)/m.factorial(k))

def secondTerm(c,p):
	return (m.pow(c*p, c)/m.factorial(int(c)))*(1/(1-p))


#Main

with open("time_delay_inputs.json") as f:
	raw_data = f.read()


time_delay_inputs = json.loads(raw_data)

calculateFullSet(time_delay_inputs)

with open("time_delay_output.json", 'w') as s:
	json.dump(time_delay_output, s, sort_keys=True)

