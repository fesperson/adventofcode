code = []

with open("day_1_input.txt", "r") as file:
    content = file.read()
    code = content.split("\n")

cur_pos = 50
password = 0

for turn in code:
    print(turn)
    if turn[0] == "L":
        cur_pos = (cur_pos - int(turn[1:])) % 100
        
    else:
        cur_pos = (cur_pos + int(turn[1:])) % 100
    if cur_pos == 0:
        password += 1
print(password)