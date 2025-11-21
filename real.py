# ------------------------------------------------------
# Name: Priyanshi Balyan
# Date: November 2025
# Title: Gradebook Analyzer
# ------------------------------------------------------

# Task 1: Project Setup and Initialization
def main_menu():
    print("\nWelcome to Gradebook Analyzer!")
    print("--------------------------------")
    print("1. Enter student data")
    print("2. Analyze statistics")
    print("3. Display grades")
    print("4. Show pass/fail summary")
    print("5. Show results table")
    print("6. Exit")

# Task 2: Data Entry (Manual Input)
def input_data():
    marks = {}
    n = int(input("\nHow many students are in the class? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        mark = float(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks

# Task 3: Statistical Analysis Functions
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    marks = sorted(marks_dict.values())
    n = len(marks)
    if n % 2 == 1:
        return marks[n // 2]
    else:
        return (marks[n // 2 - 1] + marks[n // 2]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

def show_statistics(marks_dict):
    print("\nClass Statistics:")
    print("-----------------")
    print(f"Average Marks: {calculate_average(marks_dict):.2f}")
    print(f"Median Marks : {calculate_median(marks_dict):.2f}")
    print(f"Highest Marks: {find_max_score(marks_dict)}")
    print(f"Lowest Marks : {find_min_score(marks_dict)}")

# Task 4: Grade Assignment and Distribution
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = 'A'
        elif mark >= 80:
            grade = 'B'
        elif mark >= 70:
            grade = 'C'
        elif mark >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades

def show_grade_distribution(grades):
    print("\nGrade Distribution:")
    print("-------------------")
    grade_counts = {}
    for grade in grades.values():
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    for grade, count in grade_counts.items():
        print(f"{grade}: {count} student(s)")

# Task 5: Pass/Fail Filter using List Comprehension
def pass_fail_lists(marks_dict):
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]

    print("\nPass/Fail Summary:")
    print("------------------")
    print(f"Passed Students ({len(passed_students)}): {passed_students}")
    print(f"Failed Students ({len(failed_students)}): {failed_students}")

# Task 6: Results Table and User Loop
def display_results_table(marks_dict, grades_dict):
    print("\nResults Table:")
    print("------------------------------------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade'}")
    print("------------------------------------------------")
    for name, mark in marks_dict.items():
        print(f"{name:<15}{mark:<10}{grades_dict[name]}")
    print("------------------------------------------------")

# Main program loop
def main():
    marks = {}
    grades = {}
    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            marks = input_data()
        elif choice == '2':
            if marks:
                show_statistics(marks)
            else:
                print("No data available. Please enter student data first.")
        elif choice == '3':
            if marks:
                grades = assign_grades(marks)
                show_grade_distribution(grades)
            else:
                print("No data available.")
        elif choice == '4':
            if marks:
                pass_fail_lists(marks)
            else:
                print("No data available.")
        elif choice == '5':
            if marks:
                if not grades:
                    grades = assign_grades(marks)
                display_results_table(marks, grades)
            else:
                print("No data available.")
        elif choice == '6':
            print("\nExiting Gradebook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
if __name__== "_main_":
    main()