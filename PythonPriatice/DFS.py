'''
Depth-first-search, DFS

'''
# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#def dfs(graph, start):
#    visited = []
#    stack = [start]

#    while stack:
#        n = stack.pop()
#        if n not in visited:
#            visited.append(n)
#            stack += graph[n] - set(visited)
#    return visited

#dfs(graph, 'A')

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return print(result)

dfs_paths(graph, 'A', 'F')