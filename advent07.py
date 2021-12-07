import math


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


with open("input07.txt") as f:
    lines = f.readlines()

crabs = lines[0].split(",")
crabs = [int(i) for i in crabs]

leastFuel = 999999999
for i in range(len(crabs)):
    fuelSpent = 0
    for crab in crabs:
        fuelSpent += abs(i-crab)
    if fuelSpent < leastFuel:
        leastFuel = fuelSpent
print("Part 1: " + str(leastFuel))

leastFuel = 999999999
fuelSpent = 0

for i in range(len(crabs)):
    fuelSpent = 0
    for crab in crabs:
        for j in range(abs(i - crab) + 1):
            fuelSpent += j
    if fuelSpent < leastFuel:
        leastFuel = fuelSpent
    else:
        break

print("Part 2: " + str(leastFuel))