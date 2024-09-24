def print_triples(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

N = int(input())

print_triples(N)
