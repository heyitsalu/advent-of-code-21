#if it's a tie the most used bit is 0

binary = open("input.txt", "r").read().split()
binaryCopy = binary

gamma = [""]
epsilon = [""]

bit = 0
oxygen = ""
co2 = ""

while bit < 12:
    ones = 0
    zeroes = 0

    for i in binary:
        if i[bit] == "0":
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        gamma[0] = gamma[0] + "0"
        epsilon[0] = epsilon[0] + "1"
        oxygen += "0"
    elif ones > zeroes:
        gamma[0] = gamma[0] + "1"
        epsilon[0] = epsilon[0] + "0"
        oxygen += "1"
    elif ones == zeroes:
        oxygen += "1"

    if len(binary) > 1:
        binary = [x for x in binary if x.startswith(oxygen)]

    bit += 1

bit = 0


while bit < 12:
    ones = 0
    zeroes = 0

    for z in binaryCopy:
        if z[bit] == "0":
            zeroes += 1
        elif z[bit] == "1":
            ones += 1

    if zeroes > ones:
        co2 += "1"
    elif ones > zeroes:
        co2 += "0"
    elif zeroes == ones:
        co2 += "0"

    if len(binaryCopy) > 1:
        binaryCopy = [x for x in binaryCopy if x.startswith(co2)]

    bit += 1


power = int(gamma[0], 2) * int(epsilon[0], 2)
life = int(binary[0], 2) * int(binaryCopy[0], 2)

print("gamma is ", gamma)
print("epsilon is ", epsilon)
print("power is: ", power)
print("oxygen is: ", oxygen)
print("co2 is: ", co2)
print("life is: ", life)
