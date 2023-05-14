import threading
import queue

def bfs(graph, n):
    q = queue.Queue()
    visited = []
    q.put(n)
    while not q.empty():
        nc = q.get()
        visited.append(nc)
        for i in graph[nc]:
            if i not in visited:
                q.put(i)
    return visited

graph = {0: [1, 2], 1: [2, 0], 2: [1, 4]}

v = bfs(graph, 0)
print(visited)
