import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, (sys.stdin.readline().rstrip())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

