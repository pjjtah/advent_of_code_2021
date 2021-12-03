def binary_to_decimal(binary):
    value = 0
    base = 1
    temp = int(binary)
    while temp:
        last = temp % 10
        temp = int(temp / 10)

        value += last * base
        base = base * 2
    return value


with open("input03.txt") as f:
    lines = f.readlines()
lines = [line[:-1] for line in lines]

bitCounter0 = []
bitCounter1 = []
for i in range(len(lines[0])):
    bitCounter0.append(0)
    bitCounter1.append(0)
for line in lines:
    for i in range(len(line)):
        if line[i] == "0":
            bitCounter0[i] += 1
        else:
            bitCounter1[i] += 1

gammaBinary = ""
epsilonBinary = ""
for i in range(len(lines[0])):
    if bitCounter0[i] > bitCounter1[i]:
        gammaBinary += "1"
        epsilonBinary += "0"
    else:
        gammaBinary += "0"
        epsilonBinary += "1"

gamma = binary_to_decimal(gammaBinary)
epsilon = binary_to_decimal(epsilonBinary)

print("part 1: " + str(gamma * epsilon))


bitCounter0 = 0
bitCounter1 = 0
possibleOGR = lines.copy()
possibleCSR = lines.copy()

for i in range(len(lines[0])):
    bit0 = []
    bit1 = []
    if len(possibleOGR) > 1:
        for j in range(len(possibleOGR)):
            if possibleOGR[j][i] == "0":
                bit0.append(possibleOGR[j])
            else:
                bit1.append(possibleOGR[j])
        if len(bit1) >= len(bit0):
            possibleOGR = bit1.copy()
        else:
            possibleOGR = bit0.copy()

    bit0 = []
    bit1 = []
    if len(possibleCSR) > 1:
        for j in range(len(possibleCSR)):
            if possibleCSR[j][i] == "0":
                bit0.append(possibleCSR[j])
            else:
                bit1.append(possibleCSR[j])
        if len(bit1) < len(bit0):
            possibleCSR = bit1.copy()
        else:
            possibleCSR = bit0.copy()

ogr = binary_to_decimal(possibleOGR[0])
csr = binary_to_decimal(possibleCSR[0])
print("part 2: " + str(ogr * csr))
