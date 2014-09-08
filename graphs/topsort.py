import graph, dfs

def visit(G, v, discovered=set()):
	stack = [v]
	discovered.add(v)
	visited = set()
	finishOrder = []
	while stack:
		v = stack.pop()
		if v not in visited:
			stack.append(v)
			visited.add(v)
		else:
			finishOrder.append(v)
		for u in G[v]:
			if u in stack:
				return False
			if u not in discovered:
				discovered.add(u)
				stack.append(u)
	return finishOrder



def topSort(G):
	stack = []
	for v in G:
		if v.key not in stack:
			order = visit(G, v.key, set(stack))
			if order == False:
				return "Found Cycle"
			stack.extend(order)
	stack.reverse()
	return stack