## My answer
# N = int(input())
# data = list(input().split())

# r, c = 1, 1

# for move in data:
#     if move == 'R':
#         if c + 1 > N:
#             pass
#         else:
#             c += 1
#     elif move == 'L':
#         if c - 1 < 1:
#             pass
#         else:
#             c -= 1
#     elif move == 'D':
#         if r + 1 > N:
#             pass
#         else:
#             r += 1
#     elif move == 'U':
#         if r - 1 < 1:
#             pass
#         else:
#             r -= 1

# print(r, c)

## Solution
n = int(input())
x, y = 1, 1
plans = input().split() ## 이 경우에는 list를 안 붙여도 되겠구나!

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)