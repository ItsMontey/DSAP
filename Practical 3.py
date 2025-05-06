import os

DATA_FILE = "employees.txt"
INDEX_FILE = "index.txt"

def rebuild_index():
    with open(DATA_FILE, "r") as df, open(INDEX_FILE, "w") as idxf:
        line_no = 0
        for line in df:
            if not line.startswith("DEL"):
                emp_id = line.split(",")[0]
                idxf.write(f"{emp_id},{line_no}\n")
            line_no += 1

def load_index():
    index = {}
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            for line in f:
                emp_id, line_no = line.strip().split(",")
                index[emp_id] = int(line_no)
    return index

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    salary = input("Enter Salary: ")

    # Load all employees (not deleted)
    employees = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if not line.startswith("DEL"):
                    employees.append(line.strip())

    # Add new employee and sort by ID
    new_record = f"{emp_id},{name},{designation},{salary}"
    employees.append(new_record)
    employees.sort(key=lambda x: int(x.split(",")[0]))

    # Write back to file
    with open(DATA_FILE, "w") as f:
        for emp in employees:
            f.write(emp + "\n")

    rebuild_index()
    print("Employee added successfully.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False

    if not os.path.exists(DATA_FILE):
        print("No employee data found.")
        return

    with open(DATA_FILE, "r") as f, open("temp.txt", "w") as tempf:
        for line in f:
            if line.startswith(emp_id + ",") and not line.startswith("DEL"):
                tempf.write("DEL," + line)
                found = True
            else:
                tempf.write(line)

    os.replace("temp.txt", DATA_FILE)
    rebuild_index()

    if found:
        print("Employee deleted.")
    else:
        print("Employee not found.")

def display_employee():
    emp_id = input("Enter Employee ID to search: ")
    index = load_index()

    if emp_id not in index:
        print("Employee not found.")
        return

    line_no = index[emp_id]
    with open(DATA_FILE, "r") as f:
        for i, line in enumerate(f):
            if i == line_no:
                print("\nEmployee Found:")
                parts = line.strip().split(",")
                print(f"ID: {parts[0]}")
                print(f"Name: {parts[1]}")
                print(f"Designation: {parts[2]}")
                print(f"Salary: {parts[3]}")
                return

def display_all():
    if not os.path.exists(DATA_FILE):
        print("No employee data.")
        return

    print("\nAll Employees:")
    with open(DATA_FILE, "r") as f:
        for line in f:
            if not line.startswith("DEL"):
                print(line.strip())

def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Display Employee")
        print("4. Display All Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            display_employee()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
