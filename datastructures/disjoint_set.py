
class DisjointSet(object):

	def __init__(self, value):
		self.parent = None
		self.rank = 0
		self.value = value

	def find_parent(self):
		if self.parent == None:
			return self
		self.parent = self.parent.find_parent()
		return self.parent

	def is_same_component(self, other):
		return self.find_parent() == other.find_parent()


def union(x,y):
	xRoot = x.find_parent()
	yRoot =	y.find_parent()
	if xRoot == yRoot:
		return
	if xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
	if yRoot.rank < xRoot.rank:
		yRoot.parent = xRoot
	if xRoot.rank == yRoot.rank:
		yRoot.parent = xRoot
		xRoot.rank += 1
