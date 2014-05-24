import os
import sys
sys.path.append('..')
import unittest
import graph
import dfs
class DfsTests(unittest.TestCase):
	def testBfs(self):
		G = graph.Graph()
		G.addEdge(1,2)
		G.addEdge(2,3)
		G.addEdge(4,1)
		G.addEdge(5,1)
		G.addEdge(6,1)
		G.addEdge(7,6)
		G.addEdge(3,1)
		G.addEdge(8,7)
		G.addEdge(9,8)
		G.addEdge(2,8)
		G.addEdge(9,10)
		processingOrder = []
		def processFun(v, visited):
			if v not in visited:
				processingOrder.append(v)
		dfs.dfs(G, 1, processFun, lambda v : v)
		self.failUnlessEqual(processingOrder, [1,2,8,9,10,7,6,3,4,5])

def main():
	unittest.main()

if __name__ == '__main__':
    main()