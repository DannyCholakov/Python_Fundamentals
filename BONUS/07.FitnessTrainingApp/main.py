from user import User
from exercise import Exercise
from workout import Workout
from progress_tracker import ProgressTracker


def main_menu():
    print("\nWelcome to Fitness Training App")
    print("1. Create User Profile")
    print("2. Update Profile")
    print("3. View Exercises")
    print("4. Create/Modify Workouts")
    print("5. Track Progress")
    print("6. Exit")
    return input("Choose an option: ")

def main():
    user = None
    exercise_library = [
        Exercise("Squat", "A lower body exercise targeting the quads and glutes", "Moderate"),
        Exercise("Push-Up", "An upper body exercise targeting the chest and triceps", "Easy"),
        Exercise("Deadlift", "A compound exercise targeting multiple muscle groups", "Hard")
    ]

    while True:
        choice = main_menu()
        if choice == "1":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (cm): "))
            goal = input("Enter your fitness goal: ")
            user = User(name, age, weight, height, goal)
            print("User profile created successfully!")
        elif choice == "2" and user:
            user.update_weight(float(input("Enter new weight: ")))
            user.update_goal(input("Enter new goal: "))
            print("Profile updated!")
        elif choice == "3":
            for exercise in exercise_library:
                print(exercise.display_exercise())
        elif choice == "4" and user:
            workout = Workout(input("Enter workout name: "))
            for exercise in exercise_library:
                print(exercise.display_exercise())
            while input("Add exercise? (yes/no): ").lower() == "yes":
                ex_name = input("Enter exercise name: ")
                sets = int(input("Enter sets: "))
                reps = int(input("Enter reps: "))
                rest = int(input("Enter rest time (seconds): "))
                selected_exercise = next((ex for ex in exercise_library if ex.name == ex_name), None)
                if selected_exercise:
                    workout.add_exercise(selected_exercise, sets, reps, rest)
                else:
                    print("Exercise not found!")
            workout.view_workout()
        elif choice == "5" and user:
            tracker = ProgressTracker(user)
            tracker.log_workout(input("Enter workout name: "))
            print(tracker.generate_report())
        elif choice == "6":
            break
        else:
            print("Invalid option or no user profile created!")


if __name__ == "__main__":
    main()
