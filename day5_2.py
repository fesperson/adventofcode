import numpy as np
with open("day_5_input.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")
ranges = []
ingreds = []
for row in arr:
    
    if row == "":
        break
    ranges.append(row.split("-"))

fresh_list = np.array([])
my_ranges = []
ranges = sorted(ranges, key=lambda x: int(x[0]) )

prev_n1 = int(ranges[0][0])
prev_n2 = int(ranges[0][1])

for r in range(1,len(ranges)):
    n1 = int(ranges[r][0])
    n2 = int(ranges[r][1])
    
    if prev_n2 <= n2 and prev_n2 >= n1:
        prev_n2 = n2
    if prev_n2 < n1:
        my_ranges.append([prev_n1, prev_n2])
        prev_n1 = n1
        prev_n2 = n2
my_ranges.append([prev_n1, prev_n2])

total_ranges = 0
for r in my_ranges:
    total_ranges += r[1]-r[0] + 1
print(total_ranges)