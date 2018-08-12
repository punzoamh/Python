graph = { 'A': set(['B', 'C']),
		  'B': set(['A', 'D', 'E']),
		  'C': set(['A', 'F']),
		  'D': set(['B']),
		  'E': set(['B', 'F']),
		  'F': set(['C', 'E'])}
graph2 = { 1: set([2, 3]),
	       2: set([1, 4, 5]),
		   3: set([1,5,7]),
		   4: set([2]),
		   5: set([2,3,6]),
		   6: set([5,7]),
		   7: set([3,6])}
		   
		   
def bfs(graph, start):
	#keep track of nodes visited
	explored = []
	#keep track of nodes to be checked
	queue = [start]
	#loop unitl no nodes remain unchecked
	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbours = graph[node]
			for neighbour in neighbours:
				queue.append(neighbour)
	return explored
	

def dfs(graph, vertex, path=[]):
	path += [vertex]
	for neighbor in graph[vertex]:
		if neighbor not in path:
			path = dfs(graph, neighbor, path)
	return path
	
	
print(dfs(graph2, 1))
print(bfs(graph, 'D'))
	
	
