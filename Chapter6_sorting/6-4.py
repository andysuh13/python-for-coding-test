array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1 # 왼쪽에서부터 시작
    right = end # 오른쪽에서부터 시작

    while left <= right:
        # 피벗의 왼쪽에서부터 끝까지 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 원하는 left가 된 상태. 즉, left에는 피벗보다 큰 원소의 인덱스가 저장되어 있음.

        # 끝에서부터 피벗의 왼쪽까지 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 원하는 right가 된 상태. 즉, right에는 피벗보다 작은 원소의 인덱스가 저장되어 있음.   

        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면(인덱스가 같은 경우도 포함) 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    



quick_sort(array, 0, len(array) - 1)
print(array)