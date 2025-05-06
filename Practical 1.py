# Hash table size (for simplicity, keeping it small for collision demonstration)
TABLE_SIZE = 10

# 1. Linear Probing Hash Table
class LinearProbingHashTable:
    def __init__(self):
        self.table = [None] * TABLE_SIZE
        self.comparisons = 0

    def hash_function(self, key):
        return hash(key) % TABLE_SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + 1) % TABLE_SIZE
            if index == original_index:
                raise Exception("Hash Table is Full")
        self.table[index] = (key, value)

    def search(self, key):
        self.comparisons = 0
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            self.comparisons += 1
            if self.table[index][0] == key:
                return self.table[index][1], self.comparisons
            index = (index + 1) % TABLE_SIZE
            if index == original_index:
                break
        return None, self.comparisons


# 2. Chaining Hash Table
class ChainingHashTable:
    def __init__(self):
        self.table = [[] for _ in range(TABLE_SIZE)]
        self.comparisons = 0

    def hash_function(self, key):
        return hash(key) % TABLE_SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        self.comparisons = 0
        index = self.hash_function(key)
        for k, v in self.table[index]:
            self.comparisons += 1
            if k == key:
                return v, self.comparisons
        return None, self.comparisons


# Demo and comparison
def demo():
    clients = {
        "Alice": "1234567890",
        "Bob": "9876543210",
        "Charlie": "5555555555",
        "David": "4444444444",
        "Eve": "3333333333",
        "Frank": "2222222222",
        "Grace": "1111111111",
        "Heidi": "0000000000",
        "Ivan": "9999999999",
        "Judy": "8888888888"
    }

    lp_table = LinearProbingHashTable()
    ch_table = ChainingHashTable()

    print("Inserting into both tables...\n")
    for name, number in clients.items():
        lp_table.insert(name, number)
        ch_table.insert(name, number)

    # Search for some names
    search_keys = ["Alice", "Eve", "Judy", "Zara"]  # 'Zara' doesn't exist

    print("Search Results and Comparison Counts:\n")
    for key in search_keys:
        lp_result, lp_cmp = lp_table.search(key)
        ch_result, ch_cmp = ch_table.search(key)

        print(f"Searching for '{key}':")
        print(f"  Linear Probing -> Result: {lp_result}, Comparisons: {lp_cmp}")
        print(f"  Chaining       -> Result: {ch_result}, Comparisons: {ch_cmp}")
        print()

# Run the demo
if __name__ == "__main__":
    demo()
