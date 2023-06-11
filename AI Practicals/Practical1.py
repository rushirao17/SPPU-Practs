"""
Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure
"""
#BFS-DFS

def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
    return visited

visited = []
def dfs(graph, start_node):
    visited.append(start_node)
    for neighbour in graph[start_node]:
        if neighbour not in visited:
            dfs(graph,neighbour)
    return visited

graph = {'1': ['2', '3','5'],
         '2': ['1', '5'],
         '3': ['1', '4'],
         '4': ['3','5'],
         '5': ['1','2','4']}

start_node = '1'
print('BFS:', bfs(graph, start_node))
print('DFS:', dfs(graph, start_node))
