import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

result = []

for _ in range(m):
    p, q, r = map(int, sys.stdin.readline().rstrip().split())
    if p == 0:
        union_parent(parent, q, r)
    elif p == 1:
        if find_parent(parent, q) == find_parent(parent, r):
            result.append('YES')
        else:
            result.append('NO')

for elt in result:
    print(elt)

