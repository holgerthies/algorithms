### A module to perform BFS on a Graph and applying a function when a node is discovered and processed
import graph
from Queue import Queue
def bfs(G, startNode, discover_function, process_function):
	q = Queue()
	q.put(startNode)
	visited = set([startNode])
	while not q.empty():
		v = q.get()
		process_function(v)
		for u in G[v]:
			if u not in visited:
				q.put(u)
				discover_function(u)
				visited.add(u)



