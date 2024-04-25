import sys

v, e = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] == x: # 루트인 경우
        return x
    else: # 루트가 아닌 경우
        return find_parent(parent, parent[x])

def union_parent(parent, a, b):
    a = find_parent(parent, a) # a의 루트
    b = find_parent(parent, b) # b의 루트

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    p, q = map(int, sys.stdin.readline().rstrip().split())
    union_parent(parent, p, q)


print('각 원소가 속한 집합', end=' ')
for s in range(1, v + 1):
    print(find_parent(parent, s), end=' ')
print()

print('부모 테이블:', end=' ')
for d in range(1, v + 1):
    print(parent[d], end=' ')
print()