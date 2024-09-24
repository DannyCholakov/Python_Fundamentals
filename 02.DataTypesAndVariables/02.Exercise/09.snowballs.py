n = int(input())

best_snowball_value = 0
best_snowball_data = ""

for _ in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_data = f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

if best_snowball_data:
    print(best_snowball_data)
