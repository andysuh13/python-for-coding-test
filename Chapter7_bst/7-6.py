n, m = map(int, input().split())

lst = list(map(int, input().split()))

height = max(lst)


while True:
    result = []

    for i in range(n):
        rms = lst[i] - height
        if rms > 0:
            result.append(rms)
        else:
            result.append(0)
    
    if sum(result) >= m:
        print(height)
        break
    else:
        height -= 1








    


