stack = []

# 삽입 : 5, 2, 3, 7, 삭제, 삽입 : 1, 4, 삭제

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)

stack.pop()

print(stack)
print(stack[::-1])