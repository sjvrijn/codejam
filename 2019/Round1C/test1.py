import numpy as np
from itertools import cycle

who_beats_who = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}
excludes = {
    'R': 'P',
    'P': 'S',
    'S': 'R',
}

num_cases = int(input())


def play_game():
    pass


for case in range(1, num_cases+1):
    num_opponents = int(input())

    opponents = [input() for _ in range(num_opponents)]
    max_len = max(len(op) for op in opponents)
    inf_opponents = [cycle(op) for op in opponents]

    possible_moves = [set('RPS') for _ in range(500)]
    winning_moves = [set() for _ in range(500)]

    answer = 'answer'

    for idx in range(max_len*max_len):
        idx %= 500

        remove_possible = set()
        possible_winning = set()

        for op in inf_opponents:
            remove_possible.add(who_beats_who[next(op)])
            possible_winning.add(who_beats_who[next(op)])

        possible_moves[idx] -= remove_possible
        print(possible_winning, possible_moves[idx])
        print(possible_winning.intersection(possible_moves[idx]))
        winning_moves[idx] = possible_winning.intersection(possible_moves[idx])

        if len(possible_moves[idx]) == 0:
            answer = 'IMPOSSIBLE'
            break

        if len(winning_moves[idx]) > 0:
            print(idx, winning_moves[idx])
            break

    print("Case #{case}: {answer}".format(case=case, answer=answer))
