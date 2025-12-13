import numpy as np

input = []

with open("day_3_input.txt", "r") as file:
    content = file.read()
    input = content.split("\n")

sum = 0

for bank in input:
    bank = list(map(int, bank))
    rhs = 11
    sels = []
    while rhs > 0:
        big_lhs = np.argmax(bank[0:-rhs])
        sels.append(bank[big_lhs])
        bank = bank[big_lhs+1:]
        rhs -= 1
    sels.append(max(bank))
    print(sels)
    joltage = int("".join(map(str,sels)))
    sum += joltage

print(sum)
