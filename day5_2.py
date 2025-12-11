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
for r in ranges:
    min = int(r[0])
    max = int(r[1])
    joined = False
    for i in range(len(my_ranges)):
        if min > my_ranges[i][0] and min < my_ranges[i][1] and max > my_ranges[i][1]:
            my_ranges[i][1] = max
            joined = True

        if min < my_ranges[i][0] and max > my_ranges[i][0] and max < my_ranges[i][1]:
            my_ranges[i][0] = min  
            joined = True
    if not joined:
        my_ranges.append([min,max])

my_ranges = sorted(my_ranges, key=lambda x: x[0])
for i in range(len(my_ranges) - 1):
    if my_ranges[i][1] >= my_ranges[i+1][0]:
        my_ranges[i][1] = my_ranges[i+1][1]
        my_ranges[i+1][0] = my_ranges[i][0] 
        my_ranges[i].append("delete")
for r in my_ranges:
    print(r)


total_fresh = 0
for r in my_ranges:
    if len(r) == 2:
        total_fresh += r[1] - r[0] + 1

print(total_fresh)

