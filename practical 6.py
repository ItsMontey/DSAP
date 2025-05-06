import heapq

class MarksHeap:
    def __init__(self, marks):
        self.marks = marks
        self.min_heap = marks.copy()
        self.max_heap = [-m for m in marks]  # Simulate max heap
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def get_min_marks(self):
        return self.min_heap[0] if self.min_heap else None

    def get_max_marks(self):
        return -self.max_heap[0] if self.max_heap else None


def main():
    print("Enter marks of students separated by spaces:")
    input_marks = input().split()
    marks = list(map(int, input_marks))

    heap = MarksHeap(marks)

    min_marks = heap.get_min_marks()
    max_marks = heap.get_max_marks()

    print("\n📊 Results:")
    print("Minimum marks:", min_marks)
    print("Maximum marks:", max_marks)

    print("\n🔍 Time Complexity:")
    print("Heapify: O(n)")
    print("Get min/max: O(1)")

if __name__ == "__main__":
    main()
