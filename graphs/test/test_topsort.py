import os
import sys
sys.path.append('..')
import unittest
import graph
import topsort
class TopsortTests(unittest.TestCase):
	def testTopSort(self):
		G = graph.Graph(True)
		G.addEdge(5,0)
		G.addEdge(5,2)
		G.addEdge(2,3)
		G.addEdge(3,1)	
		G.addEdge(4,0)	
		G.addEdge(4,1)			
		ts = topsort.topSort(G)
		print ts
		self.failUnless(ts.index(5) < ts.index(2))
		self.failUnless(ts.index(5) < ts.index(0))
		self.failUnless(ts.index(5) < ts.index(3))
		self.failUnless(ts.index(5) < ts.index(1))
		self.failUnless(ts.index(4) < ts.index(0))
		self.failUnless(ts.index(4) < ts.index(1))
		self.failUnless(ts.index(3) < ts.index(1))
	def testCycle(self):
		G = graph.Graph(True)
		G.addEdge(0,5)
		G.addEdge(5,2)
		G.addEdge(2,3)
		G.addEdge(3,1)	
		G.addEdge(4,0)	
		G.addEdge(4,1)	
		G.addEdge(3,0)		
		ts = topsort.topSort(G)
		self.failUnlessEqual(ts, "Found Cycle")

def main():
	unittest.main()

if __name__ == '__main__':
    main()