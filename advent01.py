with open("input01.txt") as f:
    lines = f.readlines()
measures = [int(i) for i in lines]

#part 1
previous = int(lines[0])
counter = 0
for m in measures:
    if m > previous:
        counter += 1
    previous = m
print("part 1: " + str(counter))

#part 2
previous = []
counter = 0
for m in measures:
    if len(previous) > 3:
        previous.pop(0)
    if len(previous) > 2:
        if sum(previous) < previous[1] + previous[2] + m:
            counter += 1
    previous.append(m)


print("part 2: " + str(counter))
