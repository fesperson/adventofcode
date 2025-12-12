import numpy as np
with open("day_6_input.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")

rows = []
for row in arr:
    rows.append(row.split(" "))

print(rows)
for row in rows:
    row[:] = [x for x in row if x]
ops = np.transpose(np.array(rows))
# print(ops)
total = 0
for op in ops:
    old_total = total
    if op[-1] == "*":
        total += np.prod((op[:-1]).astype(np.int64))
    else:
        total += np.sum((op[:-1]).astype(np.int64))
    print(op, total-old_total)
print(total)