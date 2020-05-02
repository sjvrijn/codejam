import numpy as np

T = int(input())


def get_route(x, y):
    num_steps = int(np.ceil(np.log2(abs(x) + abs(y) + 1)))
    steps = []

    for step_num in reversed(range(num_steps)):
        if abs(x) > abs(y):
            if x > 0:
                steps.append('E')
                x -= 2 ** step_num
            else:
                steps.append('W')
                x += 2 ** step_num
        else:
            if y > 0:
                steps.append('N')
                y -= 2 ** step_num
            else:
                steps.append('S')
                y += 2 ** step_num

    return reversed(steps)



for case in range(1, T+1):

    x, y = map(int, input().split(" "))

    if (x+y) % 2 == 0:
        result = 'IMPOSSIBLE'
    else:
        result = get_route(x, y)

    print('Case #{case}: {result}'.format(case=case, result=''.join(result)))

