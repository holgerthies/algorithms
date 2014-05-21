class Vertex:
	def __init__(self,key):
		self.key = key
		self.neighbors = {}
	def addNeighbor(self, v, weight=1):
		self.neighbors[v] = weight
	def getWeight(self, key):
		return self.neighbors[key]
	def __str__(self):
		return str(self.key)+": "+" ".join([str(x) for x in self.neighbors])
	def __contains__(self, n):
		return n in self.neighbors.keys()
	def __iter__(self):
		return iter(self.neighbors.keys())

class Graph:
	def __init__(self, directed=False):
		self.vertices = {}
		self.numVertices = 0
		self.directed = directed
	def addVertex(self, key):
		self.vertices[key] = Vertex(key)
		self.numVertices += 1
	def addEdge(self, f,t,weight=1):
		if f not in self.vertices:
			self.addVertex(f)
		if t not in self.vertices:
			self.addVertex(t)
		self.vertices[f].addNeighbor(t, weight)
		if not self.directed:
			self.vertices[t].addNeighbor(f, weight)
	def getNeighbors(self, key):
		return self.vertices[key].neighbors.keys();
	def __contains__(self, n):
		return n in self.vertices
	def __iter__(self):
		return iter(self.vertices.values())
	def __str__(self):
		s = "\n".join([str(v) for v in self])
		return s
	def __getitem__(self, key):
		return self.vertices[key] 

