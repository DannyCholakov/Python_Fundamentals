
times = list(map(int, input().split()))

middle_index = len(times) // 2

left_racer_times = times[:middle_index]
right_racer_times = times[middle_index + 1:]
right_racer_times.reverse()

def calculate_total_time(racer_times):
    total_time = 0
    for time in racer_times:
        total_time += time
        if time == 0:
            total_time *= 0.8
    return total_time

left_racer_total_time = calculate_total_time(left_racer_times)
right_racer_total_time = calculate_total_time(right_racer_times)

if left_racer_total_time < right_racer_total_time:
    print(f"The winner is left with total time: {left_racer_total_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_total_time:.1f}")
