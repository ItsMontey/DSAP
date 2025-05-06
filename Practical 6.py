class UnionFind:
    def __init__(self, n):
        # Initialize the parent and rank for union-find
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        # Find the representative of the set containing u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        # Union by rank to keep the tree shallow
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal(n, edges):
    # Sort edges based on cost
    edges.sort(key=lambda x: x[2])  # Sorting by the third element (cost)

    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for u, v, cost in edges:
        # If the nodes u and v are not connected, add the edge
        if uf.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v, cost))

    return mst_cost, mst_edges


# Example: Graph with 4 offices (nodes), 5 connections (edges)
# Edges are in the format (u, v, cost)
edges = [
    (0, 1, 10),  # Edge from office 0 to office 1 with cost 10
    (0, 2, 6),  # Edge from office 0 to office 2 with cost 6
    (0, 3, 5),  # Edge from office 0 to office 3 with cost 5
    (1, 3, 15),  # Edge from office 1 to office 3 with cost 15
    (2, 3, 4)  # Edge from office 2 to office 3 with cost 4
]

# Number of offices (nodes)
n = 4

# Solve MST using Kruskal's algorithm
mst_cost, mst_edges = kruskal(n, edges)

# Output the result
print("Minimum Cost to Connect All Offices:", mst_cost)
print("Edges in the MST:")
for u, v, cost in mst_edges:
    print(f"Office {u} - Office {v} with cost {cost}")
