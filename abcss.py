import sys
import re

vendor_prefixes = [
	'-webkit-',
	'-moz-'
	'-ms-'
]

vendor_prefixes_regex = '(' + ('|'.join(vendor_prefixes)) + ')'

def sort(rules):				
	return sorted(rules, key=lambda str : re.sub(vendor_prefixes_regex, '', str))

def format(rule, padding):	
	return rule.rjust(len(rule) + padding, '\t') + '\n'

def parse_lines(lines):
	ret = []	
	rules = []
	padding = 0
	for line in lines:
		trimmed = line.rstrip()
		
		if(len(trimmed) == 0):	
			ret.append('\n')
			continue

		last_char = trimmed[-1]		
		if(last_char == '{'):										
			for rule in sort(rules):
				ret.append(format(rule.strip(), padding))
			rules = []
			ret.append(line)
			padding += 1	
		elif(last_char == '}'):						
			for rule in sort(rules):
				ret.append(format(rule.strip(), padding))
			ret.append(line)
			rules = []
			padding -= 1
		else:
			rules.append(line)

	return ret

def main():
	filename = sys.argv[1]
	file = open(filename, 'r')
	parsed = parse_lines(file.readlines())
	file.close()
	
	outfile = open(filename, 'w')
	for line in parsed:
		outfile.write(line)
		
	outfile.close()


if __name__ == '__main__':
    main()