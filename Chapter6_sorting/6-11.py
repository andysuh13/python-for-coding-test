n = int(input())

lst = []

for _ in range(n):
    data = input().split()
    lst.append((data[0], int(data[1])))

lst = sorted(lst, key=lambda student: student[1])

for student in lst:
    print(student[0], end=' ')
print()

