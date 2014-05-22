import os
import sys
sys.path.append('..')
import unittest
import graph
import connectedcomponents
class ComponentsTest(unittest.TestCase):
	def testNumComponents(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,3)
		G.addEdge(4,1)
		G.addEdge(7,8)
		G.addEdge(8,9)
		G.addEdge(10,11)
		G.addEdge(12,13)
		G.addVertex(14)
		components = connectedcomponents.connectedComponents(G)
		self.failUnlessEqual(len(components),5)
	def testComponents(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,3)
		G.addEdge(4,1)
		G.addEdge(7,8)
		G.addEdge(8,9)
		G.addEdge(10,11)
		G.addEdge(12,13)
		G.addVertex(14)
		G.addEdge(15,16)
		components = connectedcomponents.connectedComponents(G)
		self.failUnlessEqual(components,[set([1,2,3,4]), set([7,8,9]), set([10,11]), set([12,13]), set([14]), set([15,16])])

def main():
	unittest.main()

if __name__ == '__main__':
    main()