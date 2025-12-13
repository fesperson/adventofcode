import numpy as np
with open("day_6_input.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")

rows = []
for row in arr:
    rows.append(list(row))

print(rows)
rows = np.transpose(np.array(rows))
print(rows)
total = 0
start = True
calc = []

def calculate(op, calc):
    if op == "*":
        return np.prod(calc)
    else:
        return np.sum(calc)
        

for row in rows:
    reduced = row[row != ' ']
    if start:
        op = reduced[-1]
        start = False
    if len(reduced) == 0:
        start = True
        total += calculate(op, calc)
        calc = []
    else:
        term = ""
        for char in reduced:
            if char.isnumeric():
                term += char
        calc.append(int(term))
        #print(term, op)
total += calculate(op,calc)
print(total)