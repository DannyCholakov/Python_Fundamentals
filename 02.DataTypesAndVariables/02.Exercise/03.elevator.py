persons = int(input())
capacity = int(input())

max_capacity_tours = persons // capacity
last_course_capacity = persons % capacity

if last_course_capacity == 0:
    print(max_capacity_tours)
    # print('All the people fit inside the elevator.Only one course is needed.')
else:
    print(max_capacity_tours + 1)
    # print(f'{max_capacity_tours} courses * {capacity} people + 1 course * {last_course_capacity} persons')