
class DisjointSet(object):

	def __init__(self, value):
		self.parent = None
		self.rank = 0
	
	def union(self, x,y):
		xRoot = self.find(x)
		yRoot = self.find(y)
		if xRoot == yRoot:
			return
		if xRoot.rank < yRoot.rank:
			xRoot.parent = yRoot
		if yRoot.rank < xRoot.rank:
			yRoot.parent = xRoot
		if xRoot.rank == yRoot.rank:
			yRoot.parent = xRoot
			xRoot.rank += 1

	def find(self, x):
		if x.parent == None:
			return x
		x.parent = self.find(x.parent)
		return x.parent

	def same_component(self, x,y):
		return self.find(x) == self.find(y)

