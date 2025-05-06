import queue

class Hospital:
    def __init__(self):
        # Create a priority queue
        self.patient_queue = queue.PriorityQueue()

    def add_patient(self, name, condition):
        # Assign priority based on condition
        priority_map = {
            'serious': 1,
            'non-serious': 2,
            'general': 3
        }

        condition = condition.lower()
        if condition not in priority_map:
            print(f"Unknown condition: {condition}. Cannot add patient.")
            return

        priority = priority_map[condition]
        # Add patient to the queue
        self.patient_queue.put((priority, name))
        print(f"Patient '{name}' with condition '{condition}' added to the queue.")

    def treat_patient(self):
        if self.patient_queue.empty():
            print("No patients in the queue.")
        else:
            priority, name = self.patient_queue.get()
            print(f"Treating patient: {name} (Priority {priority})")

    def show_waiting_patients(self):
        # WARNING: This is just for demonstration (not ideal for real queues)
        temp_list = list(self.patient_queue.queue)
        if not temp_list:
            print("No patients waiting.")
            return
        print("Current waiting patients (by priority):")
        for p in sorted(temp_list):
            print(f" - {p[1]} (Priority {p[0]})")

# Example usage
if __name__ == "__main__":
    h = Hospital()
    h.add_patient("Alice", "Serious")
    h.add_patient("Bob", "General")
    h.add_patient("Charlie", "Non-Serious")
    h.add_patient("David", "Serious")

    print("\n--- Waiting List ---")
    h.show_waiting_patients()

    print("\n--- Treating Patients ---")
    h.treat_patient()
    h.treat_patient()
    h.treat_patient()
    h.treat_patient()
    h.treat_patient()  # Will show empty
