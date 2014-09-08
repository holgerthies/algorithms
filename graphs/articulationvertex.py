from collections import defaultdict

def __get_discovery_times(G, s):
	''' returns the discovery-time dict by performing DFS from given start node 
	also returns a list with the nodes in post-order for the perfored DFS'''
	stack = [s]
	# a second stack to do post order traversal
	postack = []
	visited = set()
	# discovery time
	disc = dict()
	disc[s] = 0
	# current time
	time = 1
	parent = dict()
	parent[s] = -1
	# preorder traversel to set discovery time for nodes
	root_children = 0
	visited.add(s)
	while stack:
		v = stack[-1]
		finished = True
		for u in G[v].neighbors:
			if not u in visited:
				parent[u] = v
				if v == s: root_children += 1
				visited.add(u)
				stack.append(u)
				disc[u] = time
				time += 1
				finished = False
				break
		if finished:
			postack.append(v)
			stack.pop()


	return disc, postack, parent, root_children

def __get_inner_ap(G, s, disc, order, parent):
	'''	 returns a  list of articulation points
	this function receives the order the nodes are traversed as input
	'''
	aps = set() # set of articulation points
	#low(v) is the earliest discovery time for any of the neighbors of v
	#low(v) = min ({low[u] | u child of v in DFS tree}, {disc[u] | there exists a back edge from v to u}, disc[v])
	# thus low(v) is the earliest discovered vertex reachable by a path through the subtree and one back-edge 
	#an inner node v is an articulation node if no node in the subtree rooted at v has a back-edge to a node discovered before v
	low = disc.copy() 	# init with discovery time
	for v in order:
		for u in G[v].neighbors:
			if disc[u] > disc[v]: # forward edge
				low[v] = min(low[u], low[v])
				if low[u] >= disc[v] and v != s: # no subtree rooted at u can be reached by a node discovered before v
					aps.add(v)
			elif parent[u] != v: # backward edge
				low[v] = min(low[v], disc[u])
	return aps
def articulationVertex(G):
	''' iterative implementation of the algorithm to find an articulation vertex '''
	# start DFS at arbitraty node
	s = G.vertices.keys()[0]
	
	# get discovery times
	disc, postack, parent, root_children = __get_discovery_times(G,s)
	# get inner articulation points
	aps = __get_inner_ap(G, s, disc=disc, order=postack, parent=parent)
	# check if the root is an articulation point
	if root_children > 1:
		aps.add(s)
	return aps



	


