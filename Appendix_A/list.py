a = []
for i in range(1, 10):
  a.append(i)
print(a)

b = [i for i in range(20) if i % 2 == 1]
print(b)

c = [i * i for i in range(1, 10)]
print(c)

k = 10
d = [0] * k
print(d)

n = 3
m = 4
e = [[0] * m for _ in range(n)]
print(e)
e[1][1] = 5
print(e)

f = [[0] * m] * n
print(f)
f[1][1] = 5
print(f)
