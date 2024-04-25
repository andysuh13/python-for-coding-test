import sys

n = int(sys.stdin.readline().rstrip())

result = []

for _ in range(n):
    data = sys.stdin.readline().rstrip().split()
    name, score = data[0], int(data[1])
    result.append((name, score))

result.sort(key=lambda data: data[1])

for elt in result:
    print(elt[0], end=' ')
print()