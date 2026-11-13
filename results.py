# results.py
# Grading logic and class statistics.

from __future__ import annotations

from student import Student


# Give a grade based on the average score
def get_grade(average: float) -> str:
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"


# Ask for a number between 0 and 100. Keeps asking until it is valid.
def ask_score(subject: str) -> float:
    while True:
        try:
            score = float(input("Score for " + subject + " (0-100): "))
        except ValueError:
            print("Please type a number.")
            continue

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue

        return score


# Work out highest, lowest and class average of the students' averages
def class_statistics(students: list[Student]) -> tuple[float, float, float] | None:
    if len(students) == 0:
        return None
    averages: list[float] = []
    for s in students:
        averages.append(s.get_average())
    highest = max(averages)
    lowest = min(averages)
    class_avg = sum(averages) / len(averages)
    return highest, lowest, class_avg


# Sort students by average (highest first)
def sort_by_average(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda s: s.get_average(), reverse=True)


# Sort students by name (A to Z)
def sort_by_name(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda s: s.name.lower())
