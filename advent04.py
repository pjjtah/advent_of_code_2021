with open("input04.txt") as f:
    lines = f.readlines()

drawn = [int(i) for i in lines[0].split(",")]
lines.pop(0)
coupons = []
for i in range(len(lines)):
    if lines[i] == "\n":
        coupons.append([])
    else:
        coupons[len(coupons)-1].append([int(i) for i in lines[i].split()])

winners = []
winnerFound = False
lastWinnerScore = 0
for d in drawn:
    winners = []
    if len(coupons) == len(winners):
        break
    for coupon in range(len(coupons)):
        win = False
        for row in range(len(coupons[coupon])):
            if d in coupons[coupon][row]:
                c = coupons[coupon][row].index(d)
                coupons[coupon][row][c] = -1
                column = 0
                columnWin = True
                rowWin = True
                for r in coupons[coupon]:
                    if r[c] != -1:
                        columnWin = False
                        break
                for num in coupons[coupon][row]:
                    if num != -1:
                        rowWin = False
                        break
                if rowWin or columnWin:
                    unmarked = 0
                    for r in range(len(coupons[coupon])):
                        for i in coupons[coupon][r]:
                            if i != -1:
                                unmarked += i
                    lastWinnerScore = d * unmarked
                    # part 1
                    if not winnerFound:
                        print("Part 1: ")
                        print("First winner found when " + str(d) + " was drawn")

                        print("Sum of unmarked numbers in the winning coupon is: " + str(unmarked))
                        print("Answer is " + str(lastWinnerScore))
                        winnerFound = True
                    winners.append(coupon)
                    win = True
                    break
                if win:
                    break
            if win:
                break
    for w in sorted(winners, reverse=True):
        coupons.pop(w)

print("")
print("Part 2: ")
print("Last winner had score of " + str(lastWinnerScore))
