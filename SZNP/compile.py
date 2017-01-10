import rules
import re

def compile(iSource):
	#Non terminating symbols
	nts = rules.rules.keys()
	program = rules.start
	while set(nts) & set(program):
		#The catalyst is the first nts from the left
		catalyst = program[re.search("["+"".join(nts)+"]",program).span()[0]]

		#Get the list of possible transforms from the rules
		transforms = rules.rules[catalyst]

		#Get the proper transform
		transform = transforms[iSource%len(transforms)][0]
		iSource /= len(transforms)

		#Apply the transform
		program = program.replace(catalyst,transform,1)
	return program

if __name__ == "__main__":
	print compile(2390123)
