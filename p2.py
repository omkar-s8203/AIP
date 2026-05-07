# Simple A* Algorithm in Python

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
h = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 1,
    'G': 0
}

def astar(start, goal):

    open_list = [start]
    visited = []

    g = {start: 0}
    parent = {start: None}

    while open_list:

        # Find node with lowest f(n)
        current = open_list[0]

        for node in open_list:
            if g[node] + h[node] < g[current] + h[current]:
                current = node

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Shortest Path:", path)
            return

        open_list.remove(current)
        visited.append(current)

        # Check neighbors
        for neighbor, cost in graph[current]:

            if neighbor not in visited:

                new_cost = g[current] + cost

                if neighbor not in open_list:
                    open_list.append(neighbor)

                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    parent[neighbor] = current

# Function call
astar('A', 'G')