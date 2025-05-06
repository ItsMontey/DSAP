class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print("  " * level + "- " + self.name)
        for child in self.children:
            child.print_tree(level + 1)


# Sample tree construction
def build_book_tree():
    book = TreeNode("Book: Data Structures")

    # Chapter 1
    ch1 = TreeNode("Chapter 1: Introduction")
    sec1_1 = TreeNode("Section 1.1: Basics")
    sec1_2 = TreeNode("Section 1.2: Applications")

    subsec1_1_1 = TreeNode("Subsection 1.1.1: History")
    subsec1_1_2 = TreeNode("Subsection 1.1.2: Importance")
    sec1_1.add_child(subsec1_1_1)
    sec1_1.add_child(subsec1_1_2)

    ch1.add_child(sec1_1)
    ch1.add_child(sec1_2)

    # Chapter 2
    ch2 = TreeNode("Chapter 2: Trees")
    sec2_1 = TreeNode("Section 2.1: Binary Trees")
    sec2_2 = TreeNode("Section 2.2: AVL Trees")

    ch2.add_child(sec2_1)
    ch2.add_child(sec2_2)

    book.add_child(ch1)
    book.add_child(ch2)

    return book


if __name__ == "__main__":
    book_tree = build_book_tree()
    print("📚 Book Structure:\n")
    book_tree.print_tree()
