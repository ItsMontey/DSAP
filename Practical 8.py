class Node:
    def __init__(self, key, meaning):
        self.key = key
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1

class AVLDictionary:
    def __init__(self):
        self.root = None

    # Utility functions
    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Insert a keyword
    def insert(self, root, key, meaning):
        if not root:
            return Node(key, meaning)
        elif key < root.key:
            root.left = self.insert(root.left, key, meaning)
        elif key > root.key:
            root.right = self.insert(root.right, key, meaning)
        else:
            root.meaning = meaning  # Update if key already exists
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def add_keyword(self, key, meaning):
        self.root = self.insert(self.root, key, meaning)

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key, root.meaning = temp.key, temp.meaning
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_keyword(self, key):
        self.root = self.delete(self.root, key)

    def get_min_value_node(self, root):
        while root.left:
            root = root.left
        return root

    def search(self, root, key, comparisons=0):
        if not root:
            return None, comparisons
        comparisons += 1
        if key == root.key:
            return root.meaning, comparisons
        elif key < root.key:
            return self.search(root.left, key, comparisons)
        else:
            return self.search(root.right, key, comparisons)

    def update_keyword(self, key, new_meaning):
        self.add_keyword(key, new_meaning)  # insert already updates

    def in_order(self, root, reverse=False):
        if root:
            yield from self.in_order(root.right if reverse else root.left, reverse)
            yield (root.key, root.meaning)
            yield from self.in_order(root.left if reverse else root.right, reverse)

    def display_sorted(self, ascending=True):
        print("Dictionary entries:")
        for key, meaning in self.in_order(self.root, reverse=not ascending):
            print(f"{key}: {meaning}")

    def max_comparisons(self):
        return self.get_height(self.root)

# ------------------ Example Usage ------------------

d = AVLDictionary()
d.add_keyword("apple", "A fruit")
d.add_keyword("banana", "Another fruit")
d.add_keyword("cat", "An animal")
d.add_keyword("dog", "Another animal")
d.add_keyword("bat", "A flying mammal")

print("\nAscending order:")
d.display_sorted(ascending=True)

print("\nDescending order:")
d.display_sorted(ascending=False)

d.update_keyword("apple", "A crunchy fruit")
d.delete_keyword("banana")

print("\nAfter update and delete:")
d.display_sorted()

meaning, comparisons = d.search(d.root, "dog")
print(f"\nMeaning of 'dog': {meaning}")
print(f"Comparisons made: {comparisons}")
print(f"Maximum comparisons in worst-case: {d.max_comparisons()}")
print("Time complexity for search: O(log n)")
