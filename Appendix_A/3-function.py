def add(a, b):
    print('a', a)
    print('b', b)
    print('a+b', a+b)

add(3, 7)
add(b=3, a=7)
add(7, 3)

a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)

def add(a, b):
    return a + b

print(add(3, 7))

print((lambda a, b: a + b)(3, 7))
    