# reports.py
# Report card, class list and saving a report to a text file.

from __future__ import annotations

from student import Student
from results import get_grade, class_statistics, sort_by_average


# Print one student's report card
def show_report_card(s: Student) -> None:
    print("\n----- REPORT CARD -----")
    print("ID     :", s.sMatric_number)
    print("Name   :", s.name)
    print("Class  :", s.student_level)
    print("Gender :", s.gender)
    print("DOB    :", s.dob)
    print("Result entered on:", s.date_entered)
    print("-----------------------")
    for subject in s.scores:
        print(subject + ":", s.scores[subject])
    print("-----------------------")
    print("Total  :", s.get_total())
    print("Average: %.2f" % s.get_average())
    print("Grade  :", get_grade(s.get_average()))


# Print every student with total, average and grade
def show_all_results(students: list[Student]) -> None:
    if len(students) == 0:
        print("No students yet.")
        return
    print("\n%-8s %-20s %-8s %-8s %-6s" % ("ID", "Name", "Total", "Average", "Grade"))
    for s in students:
        print("%-8s %-20s %-8.1f %-8.2f %-6s" % (
            s.sMatric_number, s.name, s.get_total(), s.get_average(),
            get_grade(s.get_average())))


# Print class statistics
def show_statistics(students: list[Student]) -> None:
    stats = class_statistics(students)
    if stats is None:
        print("No students yet.")
        return
    print("\nHighest average: %.2f" % stats[0])
    print("Lowest average : %.2f" % stats[1])
    print("Class average  : %.2f" % stats[2])


# Save a simple text report to a file
def save_report(students: list[Student]) -> None:
    if len(students) == 0:
        print("No students to report.")
        return
    try:
        with open("class_report.txt", "w", encoding="utf-8") as file:
            file.write("CLASS RESULT REPORT\n")
            file.write("===================\n")
            position = 1
            for s in sort_by_average(students):
                line = str(position) + ". " + s.name + " | Total: " + str(s.get_total()) \
                       + " | Average: " + "%.2f" % s.get_average() \
                       + " | Grade: " + get_grade(s.get_average()) + "\n"
                file.write(line)
                position = position + 1
            stats = class_statistics(students)
            if stats is not None:
                file.write("\nHighest average: %.2f\n" % stats[0])
                file.write("Lowest average : %.2f\n" % stats[1])
                file.write("Class average  : %.2f\n" % stats[2])
        print("Report saved as class_report.txt")
    except OSError:
        print("Error: could not save the report.")
