def extract_person_info(lines):
    for line in lines:
        name_start = line.find('@') + 1
        name_end = line.find('|')
        name = line[name_start:name_end]

        age_start = line.find('#') + 1
        age_end = line.find('*')
        age = line[age_start:age_end]

        print(f"{name} is {age} years old.")

n = int(input())

lines = [input() for _ in range(n)]

extract_person_info(lines)
