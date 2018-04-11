import sys
def Collage():
	magazine = []
	note = []
	with open(sys.argv[1]) as f:
		n = f.readline().strip().split()
		mag = int(n[0])
		post = int(n[1])
		magazine = f.readline().strip().split()
		note = f.readline().strip().split()

	#hashmap for the magazine
	htm = {}
	for i in magazine:
		if i not in htm:
			htm[i] = 1
		else:
			htm[i] += 1
	#hashmap for the note
	htn = {}	
	for i in note:
		if i not in htn:
			htn[i] = 1
		else:
			htn[i] += 1

	for i in htn:
		if i in htm:
			if htn[i] == htm[i]:
				continue
			else:
				print("NO")
				return
		else:
			print("NO")
			return
	print("YES")

if __name__ == "__main__":
	Collage()