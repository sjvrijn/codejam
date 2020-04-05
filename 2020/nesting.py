from itertools import zip_longest
import numpy as np

T = int(input())

for case in range(1, T+1):
    s = input().strip()
    diffs = np.diff(list(map(int, '0' + s + '0')))

    result = []
    for diff, digit in zip_longest(diffs, s):
        if diff < 0:
            result.append(')' * abs(diff))
        else:
            result.append('(' * diff)

        if digit is not None:
            result.append(digit)


    print('Case #{case}: {result}'.format(case=case, result=''.join(result)))

