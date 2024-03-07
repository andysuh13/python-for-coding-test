# a = (1, 5, 10, 2, 4)
# print(sorted(a))

# result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
# print(result)

# from itertools import permutations
# data = ['A', 'B', 'C']
# result = list(permutations(data, 2))
# print(result)

# from itertools import combinations
# data = ['A', 'B', 'C']
# result = list(combinations(data, 2))
# print(result)

# from itertools import product
# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2))
# print(result)

# from itertools import combinations_with_replacement
# data = ['A', 'B', 'C']
# result = list(combinations_with_replacement(data, 2))
# print(result)

# import heapq
# def heapsort(iterable):
#     h = []
#     result = []
#     for value in iterable:
#         heapq.heappush(h, value)
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

# import heapq
# def heapsort(iterable):
#     h = []
#     result = []
#     for value in iterable:
#         heapq.heappush(h, -value)
#     for _ in range(len(h)):
#         result.append(-heapq.heappop(h))
#     return result
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

# from bisect import bisect_left, bisect_right
# a = [1,2,4,4,8]
# x = 4
# print(bisect_left(a, x))
# print(bisect_right(a, x))

from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4 ,4))
print(count_by_range(a, -1, 3))