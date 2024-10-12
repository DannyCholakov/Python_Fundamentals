def softuni_course_planning():
    # Read the initial schedule of lessons
    lessons = input().split(", ")

    while True:
        command = input()
        if command == "course start":
            break

        # Split command into parts
        parts = command.split(":")
        action = parts[0]

        if action == "Add":
            lesson_title = parts[1]
            if lesson_title not in lessons:
                lessons.append(lesson_title)

        elif action == "Insert":
            lesson_title = parts[1]
            index = int(parts[2])
            if lesson_title not in lessons and 0 <= index < len(lessons):
                lessons.insert(index, lesson_title)
            elif lesson_title not in lessons and index >= len(lessons):
                lessons.append(lesson_title)

        elif action == "Remove":
            lesson_title = parts[1]
            if lesson_title in lessons:
                lessons.remove(lesson_title)
                # Remove corresponding exercise if exists
                exercise_title = f"{lesson_title}-Exercise"
                if exercise_title in lessons:
                    lessons.remove(exercise_title)

        elif action == "Swap":
            lesson_title1 = parts[1]
            lesson_title2 = parts[2]
            if lesson_title1 in lessons and lesson_title2 in lessons:
                index1 = lessons.index(lesson_title1)
                index2 = lessons.index(lesson_title2)
                lessons[index1], lessons[index2] = lessons[index2], lessons[index1]
                # Swap exercises if they exist
                exercise1 = f"{lesson_title1}-Exercise"
                exercise2 = f"{lesson_title2}-Exercise"
                if exercise1 in lessons:
                    # Move exercise to the new position
                    lessons.remove(exercise1)
                    lessons.insert(index2 + 1, exercise1)
                if exercise2 in lessons:
                    # Move exercise to the new position
                    lessons.remove(exercise2)
                    lessons.insert(index1 + 1, exercise2)

        elif action == "Exercise":
            lesson_title = parts[1]
            exercise_title = f"{lesson_title}-Exercise"
            if lesson_title in lessons:
                if exercise_title not in lessons:
                    index = lessons.index(lesson_title)
                    lessons.insert(index + 1, exercise_title)
            else:
                lessons.append(lesson_title)
                lessons.append(exercise_title)

    # Print the final schedule
    for index, lesson in enumerate(lessons, start=1):
        print(f"{index}.{lesson}")

# Example usage:
softuni_course_planning()
