n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 범위 벗어나면 False 반환
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상, 하, 좌, 우 끝까지 ㄱㄱ
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True # 쭉 다 돌고 나면 True 반환
    
    return False # 이미 방문했거나 칸막이면 False 반환

result = 0

for i in range(n):
    for j in range(m):
        print(dfs(i, j))
        if dfs(i, j) == True:
            result += 1
print(result)
        

