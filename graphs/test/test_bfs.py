import os
import sys
sys.path.append('..')
import unittest
import graph
import bfs
class BfsTests(unittest.TestCase):
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
		processingOrder = []
		processFun = lambda v: processingOrder.append(v)
		bfs.bfs(G, 1, lambda v : v, processFun)
		self.failUnlessEqual(processingOrder, [1,2,3,4,5,6,7,8,9])

def main():
	unittest.main()

if __name__ == '__main__':
    main()