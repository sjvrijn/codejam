from __future__ import division


def kenPicks(ken, naomi):

    heavier = [block for block in ken if block > naomi]
    if not heavier:
        return min(ken)
    else:
        return min(heavier)


file = open("input4.txt", 'r')
output = open("output4.txt", 'w')
input = []

for line in file:
    line = line.split()
    if line:
        line = [float(i) for i in line]
        input.append(line)

numCases = int(input[0][0])
input = input[1:]

for i in range(numCases):

    naomi = sorted(input[i*3 + 1])
    ken = sorted(input[i*3 + 2])

    war = deceit = 0

    for block in naomi:
        pick = kenPicks(ken, block)
        if pick < block:
            war += 1
        ken.remove(pick)

    # reset!
    ken = sorted(input[i*3 + 2])

    for block in naomi:
        if block > min(ken):
            pick = kenPicks(ken, max(ken)+0.1)
            deceit += 1
        else:
            block = max(ken) - 0.00000001
            pick = kenPicks(ken, block)
        ken.remove(pick)

    output.write("Case #{}: {} {}\n".format(i+1, deceit, war))

file.close()
output.close()
