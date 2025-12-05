import re

with open("day_2_input.txt", "r") as file:
    content = file.read()
    input = content.split(",")

ids = []
for rnge in input:
    pos = rnge.split("-")
    for i in range(int(pos[0]),int(pos[1])+1):
        i_str = str(i)
        for substr in range(1,len(i_str)//2 + 1):
            # print("pattern", i_str[0:substr], i_str)
            n_matches = len(re.findall(i_str[0:substr], i_str))
            if n_matches * len(i_str[0:substr]) == len(i_str):
                if i not in ids:
                    ids.append(i)
print(sum(ids))