# -------------------------------------------------------
# gradebook.py
# Author: Priyanshi Balyan
# Date: November 5, 2025
# Title: Gradebook Analyzer
# -------------------------------------------------------


def print_menu():
    print("\n===== Gradebook Analyzer =====")
    print("1. Enter student data")
    print("2. View statistics")
    print("3. View grades summary")
    print("4. View pass/fail report")
    print("5. Display full results table")
    print("6. Exit")


# ---------------- Task 3: Statistical Analysis ---------------- #
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        return sorted_marks[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


# ---------------- Task 4: Grade Assignment ---------------- #
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def count_grades(grades):
    summary = {}
    for grade in grades.values():
        summary[grade] = summary.get(grade, 0) + 1
    return summary


# ---------------- Task 5: Pass/Fail Lists ---------------- #
def get_pass_fail_lists(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students


# ---------------- Task 6: Results Table ---------------- #
def print_results_table(marks_dict, grades):
    print("\n-----------------------------------")
    print(f"{'Name':<10} {'Marks':<10} {'Grade':<10}")
    print("-----------------------------------")
    for name in marks_dict:
        print(f"{name:<10} {marks_dict[name]:<10} {grades[name]:<10}")
    print("-----------------------------------")


# ---------------- Task 2: Manual Data Entry ---------------- #
def input_student_data():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        mark = int(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks


# ---------------- Main Program ---------------- #
def main():
    print("Welcome to the Gradebook Analyzer!")
    marks = {}
    grades = {}

    while True:
        print_menu()
        choice = input("Enter your choice (1 – 6): ")

        if choice == '1':
            marks = input_student_data()
            print("Data entry complete.")

        elif choice == '2':
            if not marks:
                print("No data available.")
                continue
            print("\n--- Statistics ---")
            print(f"Average Marks: {calculate_average(marks):.2f}")
            print(f"Median Marks: {calculate_median(marks):.2f}")
            print(f"Highest Marks: {find_max_score(marks)}")
            print(f"Lowest Marks: {find_min_score(marks)}")

        elif choice == '3':
            if not marks:
                print("No data available.")
                continue
            grades = assign_grades(marks)
            grade_summary = count_grades(grades)
            print("\n--- Grade Distribution ---")
            for g, count in grade_summary.items():
                print(f"{g}: {count}")

        elif choice == '4':
            if not marks:
                print("No data available.")
                continue
            passed, failed = get_pass_fail_lists(marks)
            print("\n--- Pass/Fail Report ---")
            print(f"Passed ({len(passed)}): {passed}")
            print(f"Failed ({len(failed)}): {failed}")

        elif choice == '5':
            if not marks:
                print("No data available.")
                continue
            if not grades:
                grades = assign_grades(marks)
            print_results_table(marks, grades)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# Run main program
