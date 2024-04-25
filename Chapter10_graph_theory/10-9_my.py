from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

indegree = [0] * (n + 1)
costs = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]


for i in range(1, n + 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(lst)):
        if j == 0:
            costs.append(lst[0])
        elif lst[j] == -1:
            break
        else:
            graph[lst[j]].append(i)
            indegree[i] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)





