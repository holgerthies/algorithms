class edgeNode:
	def __init__(self,key):
		self.key = key
		self.neighbors = {}
	def addNeighbor(self, v, weight=1):
		self.neighors[v] = weight
	def getWeight(self, key):
		return self.neighbors[key]
	def __str__(self):
		return str(self.key)+": "+str([x for x in self.neighbors])

class Graph:
	def __init__(self):
		self.vertices = {}
		self.numVertices = 0
	def addVertex(self, key):
		self.vertices[key] = Vertex(key)
		self.numVertices += 1
	def addEdge(self, f,t,weight=1):
		if f not in self.vertices:
			self.addVertex(f)
		if t not in self.vertices:
			self.addVertex(t)
		self.vertices[f].addNeighbor(self.vertices[t], weight)
	def __contains__(self, n):
		return n in self.vertices
	def __iter__(self):
		return iter(self.vertices.values())
	def __str__(self):
		s = ""
		for v in self.vertices:
			s += str(v)+"\n"
		return s

