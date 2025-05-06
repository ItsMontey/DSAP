class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.isThreaded = False  # True if right pointer is a thread

# Convert binary tree to right-threaded binary tree
def create_threaded(root):
    def convert(node, prev):
        if not node:
            return prev

        # Recursively convert left subtree
        prev = convert(node.left, prev)

        # If previous node exists and it doesn't have a right child
        if prev and prev.right is None:
            prev.right = node
            prev.isThreaded = True

        # Update previous to current
        prev = node

        # If right is not threaded, convert right subtree
        if not node.isThreaded:
            prev = convert(node.right, prev)

        return prev

    convert(root, None)
    return root

# Inorder traversal using threads
def inorder_threaded(root):
    def leftmost(node):
        while node and node.left:
            node = node.left
        return node

    current = leftmost(root)
    while current:
        print(current.key, end=" ")

        # If this node is threaded, move to in-order successor
        if current.isThreaded:
            current = current.right
        else:
            current = leftmost(current.right)

# Example tree:
#       10
#      /  \
#     5    15
#    / \     \
#   2   7     20

def build_sample_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(20)
    return root

if __name__ == "__main__":
    print("Original Binary Tree converted to Threaded Binary Tree:")
    root = build_sample_tree()
    threaded_root = create_threaded(root)

    print("In-order traversal using threads:")
    inorder_threaded(threaded_root)
