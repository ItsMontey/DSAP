# Node class to represent each element in the skip list
import random


class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


# SkipList class that implements the Skip List data structure
class SkipList:
    def __init__(self, max_level=4):
        self.max_level = max_level
        self.level = 0
        self.header = SkipListNode(None, self.max_level)

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Find the places to update at each level
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        # Insert the new node
        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = SkipListNode(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current if current and current.value == value else None

    def closest_value(self, target):
        current = self.header
        closest = None
        closest_diff = float('inf')

        # Traverse the list to find the closest value
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < target:
                current = current.forward[i]
            # Compare the current node's value with the target
            if current.forward[i]:
                diff = abs(current.forward[i].value - target)
                if diff < closest_diff:
                    closest_diff = diff
                    closest = current.forward[i].value
        return closest


# Example usage
skip_list = SkipList(max_level=4)

# Insert elements into the skip list
elements = [10, 25, 50, 75, 100, 150, 200, 300]
for elem in elements:
    skip_list.insert(elem)

# Search for an element
search_value = 75
found_node = skip_list.search(search_value)
if found_node:
    print(f"Element {search_value} found.")
else:
    print(f"Element {search_value} not found.")

# Find the closest element to a given value
target_value = 120
closest = skip_list.closest_value(target_value)
print(f"Closest value to {target_value} is {closest}.")
