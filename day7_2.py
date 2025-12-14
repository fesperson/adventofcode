import numpy as np
with open("day_7_example.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")
grid = []
for row in arr:
    grid.append(list(row))
beam_locs = np.full(len(grid[0]), ".", dtype=str)
print(beam_locs)
print(grid)
splits = 0
# I am not quite sure how to approach this one!

for i, element in enumerate(grid[0]):
    if element == "S":
        beam_locs[i] = "|"

for row in grid:
    for i, col in enumerate(row[1:]):
        if row[i] == "|" and  beam_locs[i] == "|":
            beam_locs[i] = "|"
        elif row[i] == "^" and beam_locs[i] == "|":
            beam_locs[i+1] = "|"
            beam_locs[i-1] = "|"
            beam_locs[i] = "."
            splits += 1
    print(beam_locs)
print(splits)