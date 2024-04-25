import sys
import heapq

INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    p, q, r = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append((q, r))

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_dist = 0

for d in distance:
    if d == INF:
        pass
    else:
        count += 1
        max_dist = max(max_dist, d)

print(count - 1, max_dist)








