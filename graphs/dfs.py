### A module to perform DFS on a Graph and applying a function when a node is discovered and finished
import graph
def dfs(G, startNode, discover_function, finish_function, visited=set()):
	discover_function(startNode)
	visited.add(startNode)
	for u in G[startNode]:
		if u not in visited:
			visited = dfs(G,u,discover_function,finish_function,visited)
	finish_function(startNode)
	return visited