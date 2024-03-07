# ## My answer
# n, m = map(int, input().split())
# a, b, d = map(int, input().split())
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))
# result = 0
# vst = [[0] * m for _ in range(n)]  # 방문 기록을 위한 리스트, 방문 했으면 2, 방문하지 않았으면 1 또는 0
# vst[a][b] = 2  # 초기 위치에 대하여 방문 기록

# moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
# d0 = 0

# while True:
#     # 가려는 방향의 위치 설정
#     na = a + moves[d][0]
#     nb = b + moves[d][1]

#     # 가려는 곳이 바다이거나 방문한 적이 있는 곳이라면 왼쪽으로 회전
#     if lst[na][nb] == 1 or vst[na][nb] == 2:
#         d = (d - 1) % 4 # 왼쪽으로 회전
#         if d0 == d: # 사방이 모두 바다이거나 방문한 적이 있는 곳이라면 방향을 유지한 채로 이전 위치로 돌아감
#             a = a - moves[d][0]
#             b = b - moves[d][1]
#             if lst[a][b] == 1:
#                 break
#         continue

#     # 가려는 곳이 육지이고 방문한 적이 없는 곳이라면 이동
#     elif lst[na][nb] == 0 and vst[na][nb] == 0:
#         a, b = na, nb  # 이동
#         vst[a][b] = 2  # 방문 기록
#         d0 = d # 방향 저장

# for temp in vst:
#     result += temp.count(2)
# print(result)

## Solution
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)] # 방문 기록용 리스트, 방문 했으면 1, 방문 안 했으면 0
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후, 정면에 가보지 않고 육지인 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문 기록
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전 후, 정면에 가보지 않은 곳이 없거나 바다인 경우
    else:
        turn_time += 1

    # 사방이 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우, 종료
        else:
            break
        turn_time = 0
       
print(count)    