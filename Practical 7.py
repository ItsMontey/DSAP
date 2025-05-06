def optimal_bst(keys, probs):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize for one key
    for i in range(n):
        cost[i][i] = probs[i]
        root[i][i] = i

    # l is the chain length
    for l in range(2, n + 1):  # from 2 to n
        for i in range(n - l + 1):
            j = i + l - 1
            cost[i][j] = float('inf')
            total_prob = sum(probs[i:j + 1])

            # Try all roots from i to j
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                current_cost = left_cost + right_cost + total_prob

                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost
                    root[i][j] = r

    return cost, root


def print_bst_structure(root, keys, i, j, parent=None, is_left=True):
    if i > j:
        return
    r = root[i][j]
    if parent is None:
        print(f"Root: {keys[r]}")
    else:
        direction = "left" if is_left else "right"
        print(f"{keys[r]} is the {direction} child of {keys[parent]}")

    print_bst_structure(root, keys, i, r - 1, r, True)
    print_bst_structure(root, keys, r + 1, j, r, False)


# Example usage
keys = ["A", "B", "C", "D"]
probs = [0.1, 0.2, 0.4, 0.3]

cost_matrix, root_matrix = optimal_bst(keys, probs)

print("Minimum cost of optimal BST:", cost_matrix[0][len(keys) - 1])
print("Structure of Optimal BST:")
print_bst_structure(root_matrix, keys, 0, len(keys) - 1)
