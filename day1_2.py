code = []

with open("day_1_input.txt", "r") as file:
    content = file.read()
    code = content.split("\n")

cur_pos = 50
password = 0

# slow but works!
pword = 0
cur_pos = 50
for turn in code:
    dir = 1 if turn[0] == "R" else -1
    for click in range(int(turn[1:])):
        cur_pos = cur_pos + dir 
        cur_pos = cur_pos % 100
        if cur_pos == 0:
            pword += 1
print(pword)