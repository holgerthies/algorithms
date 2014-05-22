import graph
import bfs
def connectedComponents(G):
	components = []
	c = 0
	visited = set()
	for v in G:
		if v.key not in visited:
			components.append(set())
			bfs.bfs(G,v.key, lambda x : visited.add(x), lambda x : components[c].add(x))
			c += 1
	return components