import numpy as np

input = []

with open("day_3_input.txt", "r") as file:
    content = file.read()
    input = content.split("\n")

sum = 0

for bank in input:
    bank = list(map(int, bank))
    first_idx = np.argmax(bank[0:-1])
    first = bank.pop(first_idx)
    second = max(bank[first_idx:])
    print(first,second)
    sum += int(str(first) + str(second))

print(sum)