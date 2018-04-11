import sys


def brackCheck():
	bracks = {'[':']', '(':')', '{':'}', '<':'>'}
	brack_stack = []
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for i in range(n):
			p = f.readline().strip()
			#print(i)
			for i in range(len(p)):
				brk = False
				if p[i] in bracks:
					brack_stack.append(p[i])

				elif bracks[brack_stack.pop()] == p[i]:
					continue
				else:
					print('NO')
					brk = True
					break
			if brk == False:
				print("YES")


		
if __name__ == "__main__":
	brackCheck()