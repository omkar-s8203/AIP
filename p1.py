# Implementing DFS and BFS for an Undirected Graph

from collections import deque

# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ---------------- DFS RECURSIVE ----------------
visited_dfs = set()

def dfs(vertex):
    if vertex not in visited_dfs:
        print(vertex, end=" ")
        visited_dfs.add(vertex)

        # Visit all adjacent vertices recursively
        for neighbor in graph[vertex]:
            dfs(neighbor)

# ---------------- BFS ----------------
def bfs(start):
    visited_bfs = set()
    queue = deque()

    visited_bfs.add(start)
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Visit all adjacent vertices
        for neighbor in graph[vertex]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

# ---------------- MAIN ----------------
print("Depth First Search (DFS):")
dfs('A')

print("\n")

print("Breadth First Search (BFS):")
bfs('A')