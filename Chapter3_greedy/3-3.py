## Input
N, M = map(int, input().split())

## My answer
result = 0
for _ in range(N):
    row = list(map(int, input().split()))
    if result <= min(row):
        result = min(row)
print(result)

## Solution 1
result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

## Solution 2
result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = 10001

    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)
print(result)
