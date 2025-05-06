import os
import struct

RECORD_SIZE = 32  # bytes per record (e.g., 4 bytes for int, 28 for name)

# Hash function (simple modulo)
def hash_function(key, size=100):
    return key % size

# File name
FILE_NAME = "students.dat"

# Create an empty file with n empty slots
def initialize_file(n=100):
    with open(FILE_NAME, "wb") as f:
        for _ in range(n):
            f.write(struct.pack('i28s', -1, b'-'*28))  # -1 roll indicates empty

# Insert a record using hashing
def insert_record(roll, name):
    position = hash_function(roll)
    with open(FILE_NAME, "r+b") as f:
        offset = position * RECORD_SIZE
        f.seek(offset)
        data = f.read(RECORD_SIZE)
        existing_roll, _ = struct.unpack('i28s', data)

        if existing_roll == -1 or existing_roll == roll:
            f.seek(offset)
            f.write(struct.pack('i28s', roll, name.encode().ljust(28, b' ')))
            print(f"Record inserted at position {position}.")
        else:
            print("Collision! Record not inserted.")

# Delete a record by roll number
def delete_record(roll):
    position = hash_function(roll)
    with open(FILE_NAME, "r+b") as f:
        offset = position * RECORD_SIZE
        f.seek(offset)
        data = f.read(RECORD_SIZE)
        existing_roll, _ = struct.unpack('i28s', data)

        if existing_roll == roll:
            f.seek(offset)
            f.write(struct.pack('i28s', -1, b'-'*28))
            print("Record deleted.")
        else:
            print("Record not found.")

# Display all records
def display_records():
    print("\nAll Records:")
    with open(FILE_NAME, "rb") as f:
        pos = 0
        while True:
            data = f.read(RECORD_SIZE)
            if not data:
                break
            roll, name = struct.unpack('i28s', data)
            if roll != -1:
                print(f"Pos {pos}: Roll: {roll}, Name: {name.decode().strip()}")
            pos += 1

# ------------------- Main Menu -------------------

def main():
    initialize_file(100)  # Creates file with 100 empty records

    while True:
        print("\n1. Insert Record")
        print("2. Delete Record")
        print("3. Display Records")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            roll = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            insert_record(roll, name)

        elif choice == '2':
            roll = int(input("Enter Roll Number to delete: "))
            delete_record(roll)

        elif choice == '3':
            display_records()

        elif choice == '4':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
