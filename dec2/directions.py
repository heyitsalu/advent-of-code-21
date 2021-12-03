directions = []

f = open("input.txt", "r")

depth = 0
pos = 0
aim = 0

for i in f:
    i = i.split()
    if i[0] == "up":
        depth -= int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
    else:
        pos += int(i[1])
        aim += (int(i[1])*depth)

print("part one", depth * pos)
print("part two", aim * pos)




