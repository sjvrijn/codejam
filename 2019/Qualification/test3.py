import math
import string
import numpy as np
import sys

def encypher(primes, text):
    translate = {l: p for l, p in zip(string.ascii_uppercase, primes)}
    values = [translate[l] for l in text]
    return [a * b for a, b in zip(values[:-1], values[1:])]


def decypher(cypher):

    root = int(math.sqrt(cypher[0]))
    if cypher[0] % root == 0:
        primes = [root, root]
        idx = -1
    else:
        idx = 0
        while cypher[idx] == cypher[idx+1]:
            idx += 1

        gcd = math.gcd(cypher[idx], cypher[idx+1])
        primes = [cypher[idx] // gcd, gcd, cypher[idx+1] // gcd]

    if idx > 0:
        for c in reversed(cypher[:idx]):
            primes.insert(0, c//primes[0])

    for c in cypher[idx+2:]:
        primes.append(c//primes[-1])

    translate = {prime: letter for prime, letter in zip(sorted(set(primes)), string.ascii_uppercase)}

    # print("Case #{i}: {text}".format(i=i, text=''.join([translate[p] for p in primes])))
    return ''.join([translate[p] for p in primes])




#
# N = int(input())
#
# for i in range(1, N+1):
#     max_num, length = map(int, input().split())
#     cypher = list(map(int, input().split()))


texts = [
    'CJQUIZKNOWBEVYOFDPFLUXALGORITHMS',
    'SUBDERMATOGLYPHICFJKNQVWXZ',
    'AABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'AAABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'HOHOHOSANTAABCDEFGHIJKLMNOPQRSTUVWXYZ',
]
with open('primes.txt') as f:
    all_primes = list(map(int, next(f).split()))


for t in texts:
    for _ in range(5):
        primes = sorted(np.random.choice(all_primes, 26, replace=False).tolist())

        cypher = encypher(primes, t)
        out = decypher(cypher)
        if t != out:
            print(t)
            print(cypher)
            print(out)
            print(primes)
            print()
            sys.exit(1)
