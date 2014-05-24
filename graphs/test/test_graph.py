import os
import sys
sys.path.append('..')
import unittest
import graph
class GraphTests(unittest.TestCase):
	def testAddVertices1(self):
		G = graph.Graph()
		G.addVertex(1)
		G.addVertex(2)
		G.addVertex(3)
		self.failUnlessEqual(G.numVertices, 3)
	def testAddVertices2(self):
		G = graph.Graph()
		G.addVertex(1)
		G.addVertex(2)
		G.addVertex(3)
		self.failUnless(1 in G)
		self.failUnless(2 in G)
		self.failUnless(3 in G)
	def testAddEdges1(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,3)
		self.failUnlessEqual(G.numVertices, 3)
	def testAddEdges2(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,3)
		G.addVertex(4)
		G.addEdge(4,1)
		self.failUnless(1 in G)
		self.failUnless(2 in G)
		self.failUnless(3 in G)
		self.failUnless(4 in G)
		self.failUnlessEqual(G.getNeighbors(1), [2,4])
	def testString(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,1)
		G.addEdge(4,1)
		G.addVertex(3)
		self.failUnlessEqual(str(G), "1: 2 4\n2: 1\n3: \n4: 1")
	def testGetItem(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,1)
		G.addEdge(4,1)
		G.addVertex(3)
		self.failUnless(2 in G[1])
		self.failUnless(4 in G[1])
	def testDirected(self):
		G = graph.Graph(True)
		G.addEdge(1,2)
		G.addEdge(2,1)
		G.addEdge(4,1)
		G.addVertex(3)
		self.failUnless(2 in G[1])
		self.failUnless(1 in G[2])
		self.failIf(4 in G[1])
		self.failUnless(1 in G[4])

def main():
	unittest.main()

if __name__ == '__main__':
    main()