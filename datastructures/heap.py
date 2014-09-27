from priority_queue import PriorityQueue

class heapElement(object):
	def __init__(self,id, value, priority):
		self.id = id
		self.value = value
		self.priority = priority
		self.removed = False

	def __compare__(self, other):
		return self.priority.__compare__(other)



class BinaryHeap(PriorityQueue):

	def __init__(self, lst = []):
		self._heap = lst
		self._elements = {x.id : x for x in lst}
		self._heapify()

	def _heapify(self):
		for i in range(len(self._heap)//2,-1,-1):
			self._downheap(i)
	
	def _parent(self, pos):
		return (pos-1)//2

	def _left(self, pos):
		return 2*pos+1

	def _right(self, pos):
		return 2*pos+2

	def _upheap(self, pos):
		if self.pos == 0: return
		parent = self._parent(pos)
		if self._heap[pos] > self._heap[parent]:
			self._heap[pos], self._heap[parent] = self._heap[parent], self._heap[pos]
			self._upheap(parent)

	def _downheap(self, pos):
		if pos >= len(self._heap): return 
		left, right = self._left(pos), self._right(pos)
		max_child = left if self._heap[left] > self._heap[right] else right
		if self._heap[max_child] > self._heap[pos]:
			self._heap[pos], self._heap[max_child] = self._heap[max_child], self._heap[pos]
			self._downheap(max_child)


	def insert(self, id, value, priority):
		if id in self._elements:
			self.delete(id)
		element = heapElement(id, value, priority)
		self.elements[id] = element
		self._heap.append(element)
		self._upheap(len(self._heap)-1)

	def delete(self, id):
		if id in self._elements:
			element = self._elements[id]
			element.removed = True
			del self._elements[element.id]

	def pop(self):
		while self._heap:
			element = self._heap[0].value
			self._heap[0] = self._heap[-1]
			del self._heap[-1]
			self._downheap(0)
			if not element.removed:
				del self._elements[element.id]
				return element
		raise KeyError('Can not pop from empty heap')

	def peak(self):
		return self._heap[0].value

	def update(self, id, new_priority):
		element = self._elements[id]
		self.delete(id)
		self.insert(id, element.value, new_priority)




