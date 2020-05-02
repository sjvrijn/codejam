from collections import Counter

T = int(input())

for case in range(1, T+1):

    N = int(input())
    data = sorted((input().strip().split(' ')[1] for _ in range(10000)), key=len)
    letters = set()
    for string in data:
        letters = letters.union(set(string))
        if len(letters) == 10:
            break

    starts_with = Counter(d[0] for d in data)
    zero = letters ^ set(starts_with.keys())

    letter_order = [letter for letter, count in starts_with.most_common()]
    result = list(zero) + list(letter_order)

    print('Case #{case}: {result}'.format(case=case, result=''.join(result)))
