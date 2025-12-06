with open("day_5_input.txt", "r") as file:
    content = file.read()
    arr = content.split("\n")
ranges = []
ingreds = []
switched = False
for row in arr:
    if row == "":
        switched = True
        continue
    if switched:
        ingreds.append(row)
    else:
        ranges.append(row.split("-"))

print(ranges)
print(ingreds)
fresh_count = 0
for i in ingreds:
    fresh = False
    for range in ranges:
        if int(i) >= int(range[0]) and int(i) <= int(range[1]):
            fresh = True
    if fresh:
        fresh_count += 1
print(fresh_count)