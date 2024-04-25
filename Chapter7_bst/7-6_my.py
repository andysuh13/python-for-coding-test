import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

max_height = max(data)

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for elt in data:
            if elt > mid:
                temp += (elt - mid)
            else:
                pass

        if temp == target:
            return mid
        elif temp > target:
            start = mid + 1
        else:
            end = mid - 1
    return None

print(binary_search(m, 0, max_height))
    