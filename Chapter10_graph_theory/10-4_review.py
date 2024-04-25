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


v, e = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle_check = False


for _ in range(e):
    p, q = map(int, sys.stdin.readline().rstrip().split())
    if find_parent(parent, p) == find_parent(parent, q):
        cycle = True
        break
    else:
        union_parent(parent, p, q)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

