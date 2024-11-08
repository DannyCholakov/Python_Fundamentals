students = {}

n = int(input())

for student in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

filtered_students = {}

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        filtered_students[student] = avg_grade

for student, avg_grade in filtered_students.items():
    print(f"{student} -> {avg_grade:.2f}")
