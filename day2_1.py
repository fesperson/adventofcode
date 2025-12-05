with open("day_2_input.txt", "r") as file:
    content = file.read()
    input = content.split(",")

ids = 0
for rnge in input:
    pos = rnge.split("-")
    for i in range(int(pos[0]),int(pos[1])+1):
        if len(str(i)) % 2 == 0:
            lhs = str(i)[0:len(str(i))//2]
            rhs = str(i)[len(str(i))//2:]
            if lhs == rhs:
                # print("Match", lhs,rhs)
                print("adding", i)
                ids += i
print(ids)