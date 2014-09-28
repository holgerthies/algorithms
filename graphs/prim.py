from algorithms.datastructures.heap import BinaryHeap, heapElement
def prim(G):
	""" returns minimum spanning tree of G. """
	# start with arbitrary vertix, say the first
	v = G.vertices.keys()[0]
	# edges of the spanning tree
	T = set()
	# currently in tree vertices
	V = set([v])
	# init heap with all neighbors of v
	Q = BinaryHeap([heapElement(u, (v,u), -G[v].getWeight(u)) for u in G[v]])
	total_weight = 0
	while Q._elements:
		(v,w) = Q.pop()
		if w not in V:
			T.add((v,w))
			total_weight += G[v].getWeight(w)
			V.add(w)
			# neighbors of new vertex w might have decreased priority
			for u in G[w]:
				weight = -G[w].getWeight(u)
				if u in Q:
					if weight > Q.get(u).priority:
						Q.update(u, (w,u), weight)
				else:
					Q.insert(u, (w,u), weight)
	return T, total_weight

	

	
