import numpy as np
import sys

N = int(input())

for i in range(1, N+1):
    num_workers, num_broken, _ = list(map(int, input().split()))
    attempts = min(5, int(np.ceil(np.log2(num_workers))))
    result = np.zeros((attempts, num_workers-num_broken))

    for j in range(attempts):
        test_string = ('0' * 2**j + '1' * 2**j) * (512 // 2**j)
        print(test_string[:num_workers])
        sys.stdout.flush()
        result[j] = list(map(int, input()))
        result[j] *= 2**j

    idx_offsets = np.zeros(num_workers-num_broken)
    if num_workers > 32:
        num_offsets = 0
        prev_digit = 0
        for idx, d in enumerate(result[-1]):
            if prev_digit == 16 and d == 0:
                num_offsets += 1
            prev_digit = d
            idx_offsets[idx] = num_offsets*32

    indices = np.sum(result, axis=0) + idx_offsets
    print(' '.join(map(str, sorted(set(range(num_workers)) - set(indices)))))
    sys.stdout.flush()
    verdict = input()

sys.exit(0)
