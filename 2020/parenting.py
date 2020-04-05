from operator import itemgetter
import numpy as np

T = int(input())

for case in range(1, T+1):
    
    schedule = np.zeros((2, 24*60))
    N = int(input())

    activities = []
    for i in range(N):
        activities.append((i, *tuple(map(int, input().split(' ')))))

    activities.sort(key=itemgetter(1))

    planning = [None] * N
    for idx, start, end in activities:
        
        if np.sum(schedule[0, start:end]) == 0:
            schedule[0, start:end] = 1
            planning[idx] = 'C'
        elif np.sum(schedule[1, start:end]) == 0:
            schedule[1, start:end] = 1
            planning[idx] = 'J'
        else:
            planning = ['IMPOSSIBLE']
            break

    result = ''.join(planning)
    print('Case #{case}: {result}'.format(case=case, result=result))

