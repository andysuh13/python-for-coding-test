## INPUT
# N, M, K = map(int, input().split())
# data = list(map(int, input().split()))


## Case 1
N = 5
M = 8
K = 3
data = [2, 4, 5, 4, 6]

## Case 2
# N = 5
# M = 7
# K = 2
# data = [3, 4, 3, 4, 3]

## My answer
# result = 0
# temp = data[:]

# if data.count(max(data)) >= 2:
#     result = max(data) * M
#     print(result)
# else:
#     while M != 0:
#         for _ in range(K):
#             result += max(data)
#             M -= 1
#             if M == 0:
#                 print(result)
#                 assert 0
#         max_idx = data.index(max(data))
#         result += max((data[:max_idx] + data[max_idx+1:]))
#         M -= 1
#     print(result)

## Solution 1
# data.sort()
# first = data[-1]
# second = data[-2]
# result = 0
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
        
#     if M == 0:
#         break
#     result += second
#     M -= 1
# print(result)

## Solution 2
data.sort()
first = data[-1]
second = data[-2]
result = 0

count = M // (K + 1) * K
count += M % (K + 1)

result += first * count
result += second * (M - count)

print(result)