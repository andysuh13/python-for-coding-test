## My answer
# N = int(input())
# result = 0

# h, m, s = 0, 0, 0

# while h != N + 1:
#     s += 1
#     if s == 60:
#         m += 1
#         s = 0
#     else:
#         pass
#     if m == 60:
#         h += 1
#         m = 0
#     else:
#         pass

#     if '3' in str(h) or '3' in str(m) or '3' in str(s):
#         result += 1
#     else:
#         pass
# print(result)

## Solution
h = int(input())
count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)