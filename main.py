# main.py
# Start the program here:  python main.py

from __future__ import annotations

from student import Student
from results import ask_score, sort_by_average, sort_by_name
from storage import load_students, save_students
from reports import show_report_card, show_all_results, show_statistics, save_report

# These are the 5 subjects every student must have
SUBJECTS: list[str] = ["Maths", "English", "Science", "History", "Computer"]



def find_student(students: list[Student], sMatric_number: str) -> Student | None:
    for s in students:
        if s.sMatric_number == sMatric_number:
            return s
    return None


def add_student(students: list[Student]) -> None:
    sMatric_number = input("Matric Number: ").strip()
    if sMatric_number == "":
        print("ID cannot be empty.")
        return
    if find_student(students, sMatric_number) is not None:
        print("That ID already exists.")
        return
    name = input("Full name: ").strip()
    student_level = input("Level: ").strip()
    gender = input("Gender: ").strip()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    students.append(Student(sMatric_number, name, student_level, gender, dob))
    save_students(students)
    print("Student added.")


def view_students(students: list[Student]) -> None:
    if len(students) == 0:
        print("No students yet.")
        return
    for s in students:
        print(s.sMatric_number, "-", s.name, "-", s.student_level, "-", s.gender, "-", s.dob)


def search_student(students: list[Student]) -> None:
    word = input("Enter ID or name to search: ").strip().lower()
    found = False
    for s in students:
        if word == s.sMatric_number.lower() or word in s.name.lower():
            print(s.sMatric_number, "-", s.name, "-", s.student_level)
            found = True
    if not found:
        print("No student found.")


def update_student(students: list[Student]) -> None:
    s = find_student(students, input("Enter student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    print("Press Enter to keep the old value.")
    name = input("Name (" + s.name + "): ").strip()
    student_level = input("Class (" + s.student_level + "): ").strip()
    gender = input("Gender (" + s.gender + "): ").strip()
    dob = input("DOB (" + s.dob + "): ").strip()
    if name != "":
        s.name = name
    if student_level != "":
        s.student_level = student_level
    if gender != "":
        s.gender = gender
    if dob != "":
        s.dob = dob
    save_students(students)
    print("Student updated.")


def delete_student(students: list[Student]) -> None:
    s = find_student(students, input("Enter student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    sure = input("Delete " + s.name + "? (y/n): ").lower()
    if sure == "y":
        students.remove(s)
        save_students(students)
        print("Student deleted.")


# Used for both entering and updating scores
def enter_scores(students: list[Student]) -> None:
    s = find_student(students, input("Enter student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    for subject in SUBJECTS:
        s.set_score(subject, ask_score(subject))
    save_students(students)
    print("Scores saved.")


def update_one_score(students: list[Student]) -> None:
    s = find_student(students, input("Enter student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    if len(s.scores) == 0:
        print("No scores yet. Use option 6 first.")
        return
    subject = input("Which subject? " + str(SUBJECTS) + ": ").strip().title()
    if subject not in s.scores:
        print("Subject not found.")
        return
    s.set_score(subject, ask_score(subject))
    save_students(students)
    print("Score updated.")


def report_card(students: list[Student]) -> None:
    s = find_student(students, input("Enter student ID: ").strip())
    if s is None:
        print("Student not found.")
    elif len(s.scores) == 0:
        print("This student has no scores yet.")
    else:
        show_report_card(s)


def show_menu() -> None:
    print("\n===== NMESOMA STUDENT RESULT SYSTEM =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Enter scores")
    print("7. Update a score")
    print("8. Show report card")
    print("9. List results (by average)")
    print("10. List results (by name)")
    print("11. Class statistics")
    print("12. Save report to file")
    print("0. Exit")


def main() -> None:
    students = load_students()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            enter_scores(students)
        elif choice == "7":
            update_one_score(students)
        elif choice == "8":
            report_card(students)
        elif choice == "9":
            show_all_results(sort_by_average(students))
        elif choice == "10":
            show_all_results(sort_by_name(students))
        elif choice == "11":
            show_statistics(students)
        elif choice == "12":
            save_report(students)
        elif choice == "0":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
