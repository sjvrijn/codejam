from __future__ import division


file = open("input1.txt", 'r')
output = open("output1.txt", 'w')
input = []

for line in file:
    line = line.split()
    if line:
        line = [int(i) for i in line]
        input.append(line)

numCases = input[0][0]
input = input[1:]

for i in range(numCases):
    index = i * 10
    row1 = input[index][0]
    row2 = input[index+5][0]

    set1 = set(input[index + row1])
    set2 = set(input[index + 5 + row2])

    result = len(set1 & set2)

    if result == 0:
        print "Case #{}: Volunteer cheated!".format(i+1)
        output.write("Case #{}: Volunteer cheated!\n".format(i+1))
    elif result == 1:
        print "Case #{}: {}".format(i+1, list((set1 & set2))[0])
        output.write("Case #{}: {}\n".format(i+1, list((set1 & set2))[0]))
    else:
        print "Case #{}: Bad magician!".format(i+1)
        output.write("Case #{}: Bad magician!\n".format(i+1))

file.close()
output.close()
