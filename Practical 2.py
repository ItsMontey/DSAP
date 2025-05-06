# Representing the graph using an adjacency matrix
# Nodes: A, B, C, D, E
# The graph is undirected, meaning if A is connected to B, then B is also connected to A

# Adjacency matrix representation
graph_matrix = [
    [0, 1, 1, 0, 0],  # A: connected to B, C
    [1, 0, 0, 1, 0],  # B: connected to A, D
    [1, 0, 0, 0, 1],  # C: connected to A, E
    [0, 1, 0, 0, 0],  # D: connected to B
    [0, 0, 1, 0, 0]  # E: connected to C
]

# Adjacency list representation
graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}


# DFS (Depth First Search) using adjacency matrix
def dfs_matrix(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    node_index = ord(node) - ord('A')  # Convert node 'A' to index 0, 'B' to 1, etc.

    for i in range(len(graph)):
        if graph[node_index][i] == 1:  # Check if there's an edge between node and i
            neighbor = chr(i + ord('A'))  # Convert index back to node
            if neighbor not in visited:
                dfs_matrix(graph, neighbor, visited)


# BFS (Breadth First Search) using adjacency list
from collections import deque


def bfs_list(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Test DFS on graph represented by adjacency matrix
print("DFS traversal (Adjacency Matrix):")
dfs_matrix(graph_matrix, 'A')  # Start DFS from node A
print("\n")

# Test BFS on graph represented by adjacency list
print("BFS traversal (Adjacency List):")
bfs_list(graph_list, 'A')  # Start BFS from node A
