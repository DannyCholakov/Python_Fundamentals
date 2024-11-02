students = []

while True:
    entry = input()
    if entry.islower():  # Check if the entry is the course name in lowercase
        course = entry.replace("_", " ")
        break
    name, student_id, student_course = entry.split(":")
    students.append((name, student_id, student_course))

for name, student_id, student_course in students:
    if student_course.lower() == course:
        print(f"{name} - {student_id}")
