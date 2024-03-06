n, m = map(int, input().split())
a, b, d = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
vst = lst[:]
vst[a][b] = 2

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

# start = lst[a][b]

for _ in range(4):
    na = a + moves[d]
    nb = b + moves[d]
    if lst[na][nb] == 1:  # 가려는 곳이 육지라면 이동하지 않고 캐릭터 회전만 시킴.
        d += 1
        continue

    elif lst[na][nb] == 0 and vst[na][nb] == 0:  # 가려는 곳이 바다이고 방문하지 않은 곳이라면 이동함.
        a, b = na, nb  # 이동
        vst[a][b] = 2  # 방문 기록

    if d > 3:
        d %= 4
    else:
        pass
