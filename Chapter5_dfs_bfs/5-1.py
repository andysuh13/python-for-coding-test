stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # 리스트 슬라이싱에 이런 문법도 있었구나. lst[start:end:step]. 이때 step은 옵션.