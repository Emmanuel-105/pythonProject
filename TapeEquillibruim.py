import math

def solution(A):
    array = []
    N = len(A)
    for index in range(1,N):
        first = A[0: index : 1]
        second = A[index : N : 1]
        total = abs(sum(first) - sum(second))
        array.append(total)
    return min(array)


print(solution([4,5,3,6,7,8,2,1,9,10,3]))