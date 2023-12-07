import re

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
digits = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
totPart1 = 0 
totPart2 = 0 

def part1(lines):
	somma = 0
	for line in lines:
		num = [c for c in line if c.isnumeric()]
		somma += int(num[0]+num[-1])
	return somma

def part2(lines):
	somma = 0
	r = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
	pattern = re.compile(r)
	for line in lines:
		words = []
		for word in pattern.findall(line):
			if(word in digits):
				words.append(str(digits[word]))
			else: words.append(word)			
		somma += int(words[0]+words[-1])
	return somma

totPart1 = part1(lines)
totPart2 = part2(lines)
print("part1: ", totPart1)
print("part2: ", totPart2)