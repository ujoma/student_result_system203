# Student Result Management System

A simple menu-driven Python program for managing student records and results.

## Features
- Add, view, search, update and delete students
- Enter scores for 5 subjects (Maths, English, Science, History, Computer)
- Total, average and grade (A-F) for each student
- Report card, sorting by average or name, class statistics
- Save a text report (`class_report.txt`)
- Data saved in `data/students.json` and loaded when the program starts

## How to run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run: `python main.py`

## Files
- `main.py` - menu and program start
- `student.py` - Student class
- `results.py` - grading, sorting, statistics
- `storage.py` - load and save JSON
- `reports.py` - report card and text report

## Grading
A = 70+, B = 60-69, C = 50-59, D = 45-49, F = below 45
