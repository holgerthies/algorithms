def tarjan(G):
	""" Tarjan's algorithm to find strongly connected components """
	disc = {}
	components = []
	for v in G:
		if v.key not in disc:
			__get_components(G, v.key, disc=disc, components=components)
	return components

def __get_components(G,v, stack=[], disc={}, low={}, time = 0, components=[]):
	""" find strongly connected components by starting DFS from v 
		
	"""
	stack.append(v) # add v to stack
	disc[v] = time
	low[v] = time
	time += 1
	for w in G[v].neighbors:
		if w not in disc:
			__get_components(G,w, stack, disc, low, time, components)
			low[v] = min(low[v], low[w])
		elif w in stack:
			low[v] = min(low[v], disc[w])
	if low[v] == disc[v]: # strongly connected component starting at v
		v_component = set()
		while True:
			w = stack.pop()
			v_component.add(w)
			if v==w: break
		components.append(v_component)






	
