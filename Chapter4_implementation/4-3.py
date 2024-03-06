pos = input()
count = 0

r, c = int(pos[1]), ord(pos[0])

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1),
         (2, 1)]

for move in moves:
    nr = r + move[0]
    nc = c + move[1]
    if nr < 1 or nr > 8 or nc < ord('a') or nc > ord('h'):
        pass
    else:
        count += 1

print(count)
