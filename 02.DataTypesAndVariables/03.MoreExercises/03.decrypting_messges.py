key = int(input())

n = int(input())

message = ""

for _ in range(n):
    char = input()
    decrypted_char = chr(ord(char) + key)
    message += decrypted_char

print(message)
