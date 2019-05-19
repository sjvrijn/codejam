from collections import Counter
from itertools import permutations
import numpy as np
import sys

rangers = 'ABCDE'
all_perms = list(permutations(rangers))

size = len(all_perms) - 1
num_rounds = len(rangers)


N, _ = map(int, input().split())

for i in range(N):

    arangers = np.array([['']*num_rounds for _ in range(size)])
    remaining_rangers = set(rangers)
    missing_aranger = []

    for idx in range(size):
        print(num_rounds*idx + 1)
        sys.stdout.flush()
        arangers[idx, 0] = input()


    for offset in range(1, num_rounds):
        counter = Counter(arangers[:, offset-1])
        min_ranger = min(remaining_rangers, key=lambda x: counter[x])
        missing_aranger.append(min_ranger)
        remaining_rangers.remove(min_ranger)

        for idx in np.argwhere(arangers[:, offset-1] == min_ranger):
            print(num_rounds*idx[0] + offset + 1)
            sys.stdout.flush()
            arangers[idx, offset] = input()

    missing_aranger.append(list(remaining_rangers)[0])

    print(''.join(missing_aranger))

    sys.stdout.flush()
    verdict = input()
    if verdict == 'N':
        sys.exit(0)

sys.exit(0)
