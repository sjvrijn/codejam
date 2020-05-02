import numpy as np

T = int(input())

for case in range(1, T+1):

    N = int(input())
    array = []
    for _ in range(N):
        array.append(list(map(int, input().split(' '))))

    array = np.array(array)
    trace = np.sum(np.diagonal(array))

    rows = 0
    for row in array:
        rows += len(np.unique(row)) != N

    columns = 0
    for column in array.T:
        columns += len(np.unique(column)) != N

    result = '{trace} {rows} {columns}'.format(trace=trace, rows=rows, columns=columns)

    print('Case #{case}: {result}'.format(case=case, result=result))


