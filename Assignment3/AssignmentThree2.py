import sys
'''
Min Heap code from Canvas
'''
class BinaryHeap:
	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	def __init__(self, array=None):
		if array == None:
			self.bhsize= 0
			self.length= 1025
			self.array= [None] * self.length
		else:
			self.length= len(array) + 1
			self.array= [None] * self.length
			for i in range(len (array)):
				self.array[i+1] = array[i]
			self.bhsize= self.length- 1
			i = self.length // 2
			while i > 0:
				self.sift_down(i)
				i -= 1

	def sift_down(self, i: int) -> None:
		left = 2 * i
		right = left + 1
		smallest = i
		if left <= self.bhsize and self.array[left] < self.array[smallest]:
			smallest = left
		if right <= self.bhsize and self.array[right] < self.array[smallest]:
			smallest = right
		if smallest != i:
			x = self.array[i]
			self.array[i] = self.array[smallest]
			self.array[smallest] = x
			self.sift_down(smallest)

	def sift_up(self, i: int) -> None:
		parent = i // 2
		while i > 1 and self.array[parent] > self.array[i]:
			x = self.array[parent]
			self.array[parent] = self.array[i]
			self.array[i] = x
			i = parent
			parent = i// 2

	def insert(self, x: "comparable") -> None:
		if self.bhsize >= self.length - 1:     # need to resize
			nlength = 2 * self.length
			narray= [None] * nlength
			for i in range(1, self.bhsize+1):
				narray[i] = self.array[i]
			self.length = nlength
			self.array = narray
		self.bhsize += 1
		self.array[self.bhsize] = x
		self.sift_up(self.bhsize)

	def remove(self) -> "comparable":
		if self.bhsize== 0:
			raise BinaryHeap.Underflow("remove() called on empty heap")
		minimum = self.array[1]
		self.array[1] = self.array[self.bhsize]
		self.bhsize-= 1
		self.sift_down(1)
		return minimum

	def look(self) -> "comparable":
		if self.bhsize== 0:
			raise BinaryHeap.Underflow("look() called on empty heap")
		return self.array[1]

	def size(self) -> int:
		return self.bhsize

	def is_empty(self) -> bool:
		if self.bhsize== 0:
			return True
		else:
			return False

	def to_string(self) -> str:
		if self.bhsize== 0:
			result = 'Empty'
		else:
			l = []
			for i in range(1, self.bhsize+1):
				l.append(str  (self.array[i]))
			result = ' '.join(l)
		return result

	def __len__(self) -> int:
		return self.size()

	def __str__(self) -> bool:
		return self.to_string()

	def __iter__(self) -> "iterator":
		i = 1
		while i <= self.bhsize:
			yield self.array[i]
			i += 1

'''
Min Heap code from Canvas
'''
class MaxBinaryHeap:
	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	def __init__(self, array=None):
		if array == None:
			self.bhsize= 0
			self.length= 1025
			self.array= [None] * self.length
		else:
			self.length= len(array) + 1
			self.array= [None] * self.length
			for i in range(len (array)):
				self.array[i+1] = array[i]
			self.bhsize= self.length- 1
			i = self.length // 2
			while i > 0:
				self.sift_down(i)
				i -= 1

	def sift_down(self, i: int) -> None:
		left = 2 * i
		right = left + 1
		smallest = i
		if left <= self.bhsize and self.array[left] > self.array[smallest]:
			smallest = left
		if right <= self.bhsize and self.array[right] > self.array[smallest]:
			smallest = right
		if smallest != i:
			x = self.array[i]
			self.array[i] = self.array[smallest]
			self.array[smallest] = x
			self.sift_down(smallest)

	def sift_up(self, i: int) -> None:
		parent = i // 2
		while i > 1 and self.array[parent] < self.array[i]:
			x = self.array[parent]
			self.array[parent] = self.array[i]
			self.array[i] = x
			i = parent
			parent = i// 2

	def insert(self, x: "comparable") -> None:
		if self.bhsize >= self.length - 1: 
			nlength = 2 * self.length
			narray= [None] * nlength
			for i in range(1, self.bhsize+1):
				narray[i] = self.array[i]
			self.length = nlength
			self.array = narray
		self.bhsize += 1
		self.array[self.bhsize] = x
		self.sift_up(self.bhsize)

	def remove(self) -> "comparable":
		if self.bhsize== 0:
			raise MaxBinaryHeap.Underflow("remove() called on empty heap")
		minimum = self.array[1]
		self.array[1] = self.array[self.bhsize]
		self.bhsize-= 1
		self.sift_down(1)
		return minimum

	def look(self) -> "comparable":
		if self.bhsize== 0:
			raise MaxBinaryHeap.Underflow("look() called on empty heap")
		return self.array[1]

	def size(self) -> int:
		return self.bhsize

	def is_empty(self) -> bool:
		if self.bhsize== 0:
			return True
		else:
			return False

	def to_string(self) -> str:
		if self.bhsize== 0:
			result = 'Empty'
		else:
			l = []
			for i in range(1, self.bhsize+1):
				l.append(str  (self.array[i]))
			result = ' '.join(l)
		return result

	def __len__(self) -> int:
		return self.size()

	def __str__(self) -> bool:
		return self.to_string()

	def __iter__(self) -> "iterator":
		i = 1
		while i <= self.bhsize:
			yield self.array[i]
			i += 1

def median():
	minheap = BinaryHeap()    
	maxheap = MaxBinaryHeap()
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		z = 0
		y = 0
		#check first two elements, whichever is lower, put in the maxheap and the larger element in the minheap.
		nums = []
		if n == 1: #if we have just one element, print that element and return
			r = f.readline().strip().split()
			x = int(r[0])
			print(x)
			return
		for i in range(n):
			r = f.readline().strip().split()
			x = int(r[0])
			nums.append(x)
			if len(nums) == 1:
				print(nums[0]) #print out the first element of the list
		#print("List of numbers: ", nums)
		n0 = nums[0]
		n1 = nums[1]
		print((n0 + n1) / 2) #print the median of the first two numbers, which is just the average of the two numbers. 
		if n0 >= n1: #the larger number goes into the minheap, the smaller into the maxheap. 
			maxheap.insert(n1)
			minheap.insert(n0)
			nums = nums[2:] #Once we are done with the first two elements of the list, we can iterate through the rest which is why I modified the list.
		else:
			maxheap.insert(n0)
			minheap.insert(n1)
			nums = nums[2:]


		for i in nums:
			median = 0
			if len(maxheap) == len(minheap): 
				if i <= maxheap.look(): #check if the current element is less than the max in the maxheap, then put into the maxheap
					maxheap.insert(i)
					median = maxheap.look() #with more elements in maxheap, the maxheap root is the median.
				else:
					minheap.insert(i)
					median = minheap.look() #with more elements in minheap, the minheap root is the median.

			elif len(minheap) > len(maxheap):
				if minheap.look() < i: 
					maxheap.insert(minheap.remove()) #move the root of the minheap to the max heap to make room for the new node inserted to the minheap
					minheap.insert(i) #now put the element into the minheap.
					
				else:
					maxheap.insert(i)
				median = ((maxheap.look() + minheap.look()) / 2) #since the heaps are now balanced, the median is just the average of the two roots.


			else: 
				if maxheap.look() > i:
					minheap.insert(maxheap.remove())
					maxheap.insert(i)
					
				else:
					minheap.insert(i)
				
				
				median = ((maxheap.look() + minheap.look()) / 2)
			
			print(median)
		


		


if __name__ == "__main__":
	median()