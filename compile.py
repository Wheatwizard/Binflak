import sys
from ebin import compactEBin

charMap = {
	"(" : 1,
	"[" : 2,
	"{" : 3,
	"<" : 4,
	")" : 0,
	"]" : 0,
	"}" : 0,
	">" : 0,
}

def compileEBin(brainSource, debug = False):
	binSource = 0
	for char in brainSource[::-1]:
		binChar = charMap[char]
		
		if debug: print(binChar)
		
		binSource *= 5
		binSource += binChar
	return binSource

def compile(brainSource, debug = False):
	return compactEBin(compileEBin(brainSource, debug))

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("usage: compile.py output_file input_brainflak_program")
	else:
		binSource = compile(sys.argv[2])
		with open(sys.argv[1],'wb') as f:
			while binSource > 0:
				f.write(bytes([binSource % 256]))
				binSource //= 256
