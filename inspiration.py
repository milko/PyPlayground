import collections

graph = {"A": set(["B", "C"]),
         "B": set(["A", "D", "E"]),
         "C": set(["A", "F"]),
         "D": set(["B"]),
         "E": set(["B", "F"]),
         "F": set(["C", "E"])}

print("DFS")
def dfs(graph, start):
    visited, stack = set(), [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

x = dfs(graph, "A")
print(x)

print("\nDFS Recursive")
def dfsRec(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfsRec(graph, next, visited)
    return visited

x = dfsRec(graph, "A")
print(x)

print("\nDFS with paths")
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

x = list(dfs_paths(graph, "A", "F"))
print(x)

print("\nDFS Recursive with paths")
def dfs_pathsRec(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_pathsRec(graph, next, goal, path + [next])

x = list(dfs_pathsRec(graph, "A", "F"))
print(x)

print("\nBFS")
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

x = bfs(graph, "A")
print(x)

print("\nBFS with paths")
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
                # return path + [goal]
            else:
                queue.append((next, path + [next]))

x = list(bfs_paths(graph, "A", "F"))
print(x)

print("\nBFS shortest path")
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

x = shortest_path(graph, "A", "F")
print(x)

# small_graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'A'],
#     'C': ['A'],
#     'D': ['B']
# }

print("\nDFS alternative")
def dfs_alt(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

x = dfs_alt(graph, "A", "F")
print(str(x))

print("\nBFS alternative")
def bfs_alt(graph, start, goal):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # queue.appendleft(neighbor)
                    queue.insert(0, neighbor)

x = bfs_alt(graph, "A", "F")
print(str(x))
