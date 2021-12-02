with open("input02.txt") as f:
    lines = f.readlines()

#part 1
x = 0
y = 0
for line in lines:
    command = line.split()

    if command[0] == "forward":
        x += int(command[1])
    elif command[0] == "down":
        y += int(command[1])
    elif command[0] == "up":
        y -= int(command[1])

print("part1: " + str(x*y))

#part 2
x = 0
y = 0
aim = 0
for line in lines:
    command = line.split()

    if command[0] == "forward":
        x += int(command[1])
        y += int(command[1]) * aim
    elif command[0] == "down":
        aim += int(command[1])
    elif command[0] == "up":
        aim -= int(command[1])

print("part2: " + str(x*y))