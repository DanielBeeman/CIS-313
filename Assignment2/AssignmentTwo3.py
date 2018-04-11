import queue
import sys


'''
I was unable to finish this part of the project. I was aiming for O(n^2) runtime but was unable to get it to work.
I believe I was close, my issue was iterating through the differences of the restaurants which would cause a third
for loop to be run because I would need to update each individual restaurant energy data each time I tried a new cycle.
This was a rough week because of the CIS 314 midterm. I tried my best.

'''


def rest_Cycle():
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())


		nrgy_Data = []
		q = queue.Queue()
		diff_Data = [None] * n
		diff=0;
		for i in range(n):
			r = f.readline().strip().split() #creates a two element array of string types.
							 			 #appends it to our list
			one = r[0]						 #access the first of the two elements
			two = r[1]						 #access the second of the two elements
			one = int(one)					 #converts to int
			two = int(two)		
			nrgy_Data.append(r) 			 #converts to int
			q.put(nrgy_Data[i])
			diff = one - two
			r.append(diff)				 #the difference of energy after a visit to the i-th restaurant
			print(r)
			diff_Data[i] = diff

		def good_start(qu):
			for i in range(n):	#going through all elements in the queue
				if diff_Data[i] >= 0:
					print("Working so far at index:", i)
					print(diff_Data[i])
				else:
					print("This restaurant cycle will not work. Failed at index", i)
					temp = qu.get()
					print("all elements in list:",temp)
					print("The difference data to update:",temp[2]) #then update the list of difference data
					qu.put(temp)
					diff_Data[i] = temp[2]
					return
			print("This walkthrough works!")
			return True
		#check that the walk through the elements works
		#if not, pop from the queue and then push to the queue

		for i in range(n):
			print("starting loop iteration:", i)
			if (good_start(q) == True):
				print("This is the restaurant with lowest index that works: ",i)
				break
			else:
				diff_Data[i]
				continue
		



if __name__ == "__main__":
	rest_Cycle()