def do_move(X, Y, direction):
    if direction == 'N':
        return X, Y+1
    elif direction == 'S':
        return X, Y-1
    elif direction == 'E':
        return X+1, Y
    elif direction == 'W':
        return X-1, Y
    raise ValueError("invalid direction {}".format(direction))


def do_A(X, Y, route):
    for time, direction in enumerate(route, start=1):
        X, Y = do_move(X, Y, direction)
        if abs(X) + abs(Y) <= time:
            return time
    else:
        return "IMPOSSIBLE"


def main():
    T = int(input())
    for case in range(1, T+1):
        X, Y, route = input().strip().split(' ')
        result = do_A(int(X), int(Y), route)
        print('Case #{case}: {result}'.format(case=case, result=result))


if __name__ == '__main__':
    main()
