n = int(input())
my = list(map(int, input().split()))
m = int(input())
cst = list(map(int, input().split()))

result = []

for i in range(m):
    if cst[i] in my:
        result.append('yes')
    else:
        result.append('no')

for i in range(len(result)):
    print(result[i], end=' ')
