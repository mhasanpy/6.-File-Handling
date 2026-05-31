# practice_06_file_handling.py
"""
File Handling Practice
"""

import json
import csv

# Exercise 1: Write and Read Text Files
print("=== Exercise 1: Text Files ===")
def create_notes_file():
    notes = [
        "Day 1: Learned Python basics",
        "Day 2: Practiced loops and conditions",
        "Day 3: Started functions",
        "Day 4: Working with lists and dictionaries"
    ]
    
    # Write to file
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")
    
    # Read from file
    with open("notes.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)

create_notes_file()

# Exercise 2: CSV File Handling
print("\n=== Exercise 2: CSV Files ===")
def manage_student_csv():
    students_data = [
        ["Name", "Age", "Grade"],
        ["Alice", 20, "A"],
        ["Bob", 22, "B"],
        ["Charlie", 21, "A"],
        ["Diana", 23, "C"]
    ]
    
    # Write to CSV
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students_data)
    
    # Read from CSV
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:10} {row[1]:3} {row[2]:5}")

manage_student_csv()

# Exercise 3: JSON Data Storage
print("\n=== Exercise 3: JSON Files ===")
def manage_tasks_json():
    tasks = {
        "user": "John",
        "tasks": [
            {"id": 1, "title": "Complete Python exercise", "completed": False},
            {"id": 2, "title": "Read Django documentation", "completed": True},
            {"id": 3, "title": "Practice file handling", "completed": False}
        ]
    }
    
    # Write to JSON
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    
    # Read from JSON
    with open("tasks.json", "r") as file:
        loaded_tasks = json.load(file)
        print(f"Tasks for {loaded_tasks['user']}:")
        for task in loaded_tasks['tasks']:
            status = "✓" if task['completed'] else "✗"
            print(f"  {status} {task['title']}")

manage_tasks_json()