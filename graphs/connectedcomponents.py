import bfs
def connectedComponents(G):
	components = []
	c = 0
	visited = set()
	for v in G:
		if v.key not in visited:
			components.append(set())
			bfs.bfs(G,v.key, discover_function = lambda x : visited.add(x), process_function = lambda x : components[c].add(x))
			c += 1
	return components