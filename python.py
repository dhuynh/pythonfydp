

lines = []

with open("solution.txt") as f:
	lines = f.read().splitlines()

with open('transformedsolution.txt', 'w') as s:
	s.write(lines)