# storage.py
# Saving and loading data from a JSON file.

from __future__ import annotations

import json
import os

from student import Student, student_from_dict

DATA_FILE = os.path.join("data", "students.json")


# Save all students to the file
def save_students(students: list[Student]) -> None:
    try:
        if not os.path.exists("data"):
            os.makedirs("data")
        data = []
        for s in students:
            data.append(s.to_dict())
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Error: could not save the data.")


# Load students from the file when the program starts
def load_students() -> list[Student]:
    students: list[Student] = []
    # If the file does not exist yet, just return an empty list
    if not os.path.exists(DATA_FILE):
        return students
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        for item in data:
            students.append(student_from_dict(item))
    except (OSError, ValueError, KeyError):
        print("Warning: data file could not be read. Starting empty.")
        students = []
    return students
