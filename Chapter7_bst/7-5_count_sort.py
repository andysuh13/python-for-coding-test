import sys

n = int(sys.stdin.readline().rstrip())
array = [0] * 1000001

for i in sys.stdin.readline().rstrip().split():
    array[int(i)] = 1

m = int(sys.stdin.readline().rstrip())
data_2 = list(map(int, sys.stdin.readline().rstrip()))

for elt in data_2:
    if array[elt] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()

