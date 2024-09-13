number = 12
numberFloat = 1.20
string = "Hello World"
boolean = False
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

result1 = 10 + 30 # => 40
result2 = 40 - 10 # => 30
result3 = 50 * 5  # => 250
result4 = 16 / 4  # => 4.0 (Float Division)
result5 = 16 // 4 # => 4 (Integer Division)
result6 = 25 % 2  # => 1
result7 = 5 ** 3  # => 125

counter = 0
counter += 10           # => 10
counter = 0
counter = counter + 10  # => 10
message = "Part 1."
message += "Part 2." # => Part 1.Part 2.


print("Hello, World!")

print('You\'re') # with ' use \ and '

msg = "Hello, World!"
print(msg[2:5]) # => llo

website = 'Quickref.ME'
print(f"Hello, {website}") # Hello, Quickref.ME

num = 10
print(f'{num} + 10 = {num + 10}') # 10 + 10 = 20

# IF STATEMENT
num = 200
if num > 0:
    print("num is greater than 0")
else:
    print("num is not greater than 0")

# LIST
mylist = []
mylist.append(1) # add number 1 to the back of the list
mylist.append(2) # add number 2 to the back of the list
for item in mylist:
    print(item) # prints out 1,2

# FOR LOOP
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")

# CUTTING STRINGS
stringOne = 'kitty'
stringTwo = 'doggy'
newWord = ""
oldWord = ""
n = 1
for i in range(len(stringOne)):
    newWord += stringTwo[:n] + stringOne[n:] # :n => characters before n / n: => characters after
    n += 1
    if newWord != stringOne and newWord != oldWord:
        print(newWord)
        oldWord = newWord
        newWord = ""
    else:
        newWord = ""
        continue


# WHILE LOOP
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1

#N FUNCTIONS
def my_function():
  print("Hello from a function")

my_function() # => calling function



