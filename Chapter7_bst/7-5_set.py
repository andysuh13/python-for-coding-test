import sys

n = int(sys.stdin.readline().rstrip())
data_1 = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
data_2 = list(map(int, sys.stdin.readline().rstrip().split()))

for elt in data_2:
    if elt in data_1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()

