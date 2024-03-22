n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()

lst.reverse()

for i in range(len(lst)):
    print(lst[i], end=' ')
print()