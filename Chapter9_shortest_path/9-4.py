import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    r, s = map(int, sys.stdin.readline().rstrip().split())
    graph[r][s] = 1
    graph[s][r] = 1

x, k = map(int, sys.stdin.readline().rstrip().split())

for p in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][p] + graph[p][b])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

