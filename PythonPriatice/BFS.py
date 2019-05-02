'''
Breadth-first-search, BFS

'''
# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#def bfs(graph, start):
#    visited = []
#    queue = [start]

#    while queue:
#        n = queue.pop(0)
#        if n not in visited:
#            visited.append(n)
#            print(graph[n], set(visited))
#            queue += graph[n] - set(visited)
#    return print(visited)

#bfs(graph, 'A')


# 응용 최단거리 BFS 이용
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return print(result)

bfs_paths(graph, 'A', 'F')
