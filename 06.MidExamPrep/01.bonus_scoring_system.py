import math

# Input for number of students, lectures, and additional bonus
number_of_students = int(input("Enter the number of students: "))
number_of_lectures = int(input("Enter the number of lectures: "))
additional_bonus = int(input("Enter the additional bonus: "))

# Initialize variables to track the best score and attendance
max_student_bonus = 0
max_attended_lectures = 0

# Loop through each student to calculate bonuses
for _ in range(number_of_students):
    student_attended = int(input("Enter the number of lectures attended by the student: "))

    # Calculate total bonus for the student
    total_bonus = (student_attended / number_of_lectures) * (additional_bonus + 5)

    # Update max scores if current student has a higher bonus
    if total_bonus > max_student_bonus:
        max_student_bonus = total_bonus
        max_attended_lectures = student_attended

# Print results
print(f"Max Bonus: {math.ceil(max_student_bonus)}.")
print(f"The student has attended {max_attended_lectures} lectures.")
