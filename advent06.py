with open("input06.txt") as f:
    lines = f.readlines()

fish = lines[0].split(",")
fish = [int(i) for i in fish]

for i in range(80):
    add = []
    for j in range(len(fish)):
        if fish[j] == 0:
            add.append(8)
            fish[j] = 6
        else:
            fish[j] -= 1
    fish += add

print("Part 1: " + str(len(fish)))

with open("input06.txt") as f:
    lines = f.readlines()

fish = lines[0].split(",")
fish = [int(i) for i in fish]

states = [0] * 9
for f in fish:
    states[f] += 1

for i in range(256):
    new_states = [0] * 9
    new_states[0] = states[1]
    new_states[1] = states[2]
    new_states[2] = states[3]
    new_states[3] = states[4]
    new_states[4] = states[5]
    new_states[5] = states[6]
    new_states[6] = states[7]
    new_states[7] = states[8]
    new_states[6] += states[0]
    new_states[8] = states[0]
    states = new_states

print("Part 2: " + str(sum(states)))