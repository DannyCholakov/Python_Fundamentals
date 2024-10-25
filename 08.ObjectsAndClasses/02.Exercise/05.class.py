class Class:
    student_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < self.student_count:  # Check if there's room for more students
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return round(sum(self.grades) / len(self.grades), 2)
        return 0.0

    def __repr__(self):
        students_list = ", ".join(self.students)  # Join student names with ', '
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students_list}. Average grade: {average_grade:.2f}"
