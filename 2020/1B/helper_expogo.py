import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from pprint import pprint


def get_new_positions(x, y, steps, stepsize):
    return (x+stepsize, y, steps+'E'), \
           (x-stepsize, y, steps+'W'), \
           (x, y+stepsize, steps+'N'), \
           (x, y-stepsize, steps+'S')


num_steps = 2
positions = [(0,0,'')]
shortest_paths = {(0,0): ''}


# field_radius = 2**num_steps
# positions = [(field_radius,field_radius)]
# field = np.ones((2*field_radius+1, 2*field_radius+1)) * -1
# field[positions[0]] = 0



for step in range(num_steps):
    stepsize = 2**step

    positions = {
        newpos
        for pos in positions
        for newpos in get_new_positions(*pos, stepsize)
    }

    for x, y, path in positions:
        if (x,y) not in shortest_paths:
            shortest_paths[(x,y)] = path

    print(step)
    pprint(shortest_paths)

    # print(f"step {step+1}: {len(positions)}")
    #
    # for pos in positions:
    #     if field[pos] == -1:
    #         field[pos] = step+1
#
# plt.imshow(field)
# plt.show()



def get_route(x, y):
    if x == 0 and y == 0:
        return ''

    num_steps = int(np.ceil(np.log2(abs(x) + abs(y))))
    steps = []
    print(list(range(num_steps - 1, -1, -1)))
    for step_num in range(num_steps - 1, -1, -1):
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

    return ''.join(reversed(steps))


for x,y in shortest_paths:
    try:
        assert get_route(x, y) == shortest_paths[(x,y)]
    except AssertionError as e:
        print(x, y)
        print(f'route : {get_route(x, y)}')
        print(f'path  : {shortest_paths[(x, y)]}')
        raise e

