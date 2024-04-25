import sys

n = int(sys.stdin.readline().rstrip())
data_1 = list(map(int, sys.stdin.readline().rstrip().split()))
data_1.sort()
m = int(sys.stdin.readline().rstrip())
data_2 = list(map(int, sys.stdin.readline().rstrip().split()))

# # 시간 초과 풀이
# for elt in data_2:
#     if elt in data_1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
# print()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

for target in data_2:
    print(binary_search(data_1, target, 0, n - 1), end=' ')
print()
