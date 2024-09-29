def josephus_permutation(people, k):
    result = []
    index = 0

    while len(people) > 0:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return result

people_input = input().split()
k = int(input())
people = list(map(int, people_input))
execution_order = josephus_permutation(people, k)

print(f"[{','.join(map(str, execution_order))}]")
