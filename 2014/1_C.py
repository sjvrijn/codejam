from __future__ import division


file = open("input3.txt", 'r')
output = open("output3.txt", 'w')
input = []

for line in file:
    line = line.split()
    if line:
        line = [float(i) for i in line]
        input.append(line)

numCases = int(input[0][0])
input = input[1:]

for i in range(numCases):


    output.write("Case #{}: {}\n".format(i+1, result))

file.close()
output.close()
