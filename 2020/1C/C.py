from collections import Counter


def do_C(D, slices):
    if len(slices) == 1:
        return D-1

    c = Counter(slices)
    most_common_size, most_common_num = c.most_common(1)[0]
    if most_common_num >= D:
        return 0

    unique_sizes = set(slices)
    for size in slices:
        if size*2 in unique_sizes:
            return 1

    at_least_two = [size for size, num in c.most_common() if num >= 2]
    for num in at_least_two:
        if num != max(slices):
            return 1

    return D-1


T = int(input())
for case in range(1, T+1):
    N, D = map(int, input().strip().split(' '))
    slices = list(sorted(map(int, input().strip().split(' '))))

    print('Case #{case}: {result}'.format(case=case, result=do_C(D, slices)))
