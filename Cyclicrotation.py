def rotate(A):
    a = A.pop()
    A.insert(0, a)

def solution(A, K):
    if A == []:
        return []
    stopper = 0
    while K > stopper:
        rotate(A)
        stopper += 1
    return A


print(solution([4,6,7,8,3,4,5], 4))
#solution([4,6,7,8,3,4,5], 4)