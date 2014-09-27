from algorithms.datastructures.heap import BinaryHeap
def prim(G):
	""" returns minimum spanning tree of G. """
	# start with arbitrary vertix, say the first
	v = G[0]
	Q = BinaryHeap()
	
