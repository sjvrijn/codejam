N = int(input())

for i in range(1, N+1):
    size = int(input())
    path = input()

    inv = {'E': 'S', 'S': 'E'}

    my_path = [inv[s] for s in path]

    print("Case #{i}: {my_path}".format(i=i, my_path=''.join(my_path)))

