import numpy as np

num_cases = int(input())

for case in range(1, num_cases+1):
    num_people, size = map(int, input().split())

    manhattan = np.zeros((size+1, size+1))
    for p in range(num_people):
        x, y, direction = input().split()
        x, y = int(x), int(y)
        if direction == 'N':
            manhattan[:,y+1:] += 1
        elif direction == 'S':
            manhattan[:,:y-1] += 1
        elif direction == 'E':
            manhattan[x+1:,:] += 1
        elif direction == 'W':
            manhattan[:x-1,:] += 1


    manhattan_max = np.max(manhattan)

    print(manhattan.T)
    print(np.argwhere(manhattan)[0])

    X = min(np.argmax(manhattan == manhattan_max, axis=0))
    Y = np.argmin(manhattan[X] == manhattan_max)

    print("Case #{case}: {x} {y}".format(case=case, x=X, y=Y))
