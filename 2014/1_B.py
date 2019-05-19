from __future__ import division


file = open("input2.txt", 'r')
output = open("output2.txt", 'w')
input = []

for line in file:
    line = line.split()
    if line:
        line = [float(i) for i in line]
        input.append(line)

numCases = int(input[0][0])
input = input[1:]

baseIncome = 2

for i in range(numCases):
    cost, extra, target = input[i]

    result = target / baseIncome
    faster = True

    farmCost = 0
    numFarms = 0
    income = baseIncome

    while faster:

        farmCost += cost/income
        numFarms += 1
        income += extra

        newBest = farmCost + target/income

        if newBest < result:
            result = newBest
        else:
            faster = False

    #print "Case #{0}: {1:.7f}".format(i+1, result)
    output.write("Case #{0}: {1:.7f}\n".format(i+1, result))

file.close()
output.close()
